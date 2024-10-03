from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm  
from plants.models import Plants_Types, CategoryPlant
from .models import FavoritePlant
from django.urls import reverse
#register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            auth_login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'green_world/register.html', {'form': form})
#login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            plant_to_save = request.session.pop('plant_to_save', None)
            next_url = request.POST.get('next', '')  
            if plant_to_save:
                plant = get_object_or_404(Plants_Types, pk=plant_to_save)
                FavoritePlant.objects.get_or_create(user=user, plant=plant)
                return redirect('favorites')
            
            return redirect(next_url or 'index')  

        else:
            messages.error(request, 'Invalid username or password.')
    else:
        next_url = request.GET.get('next', '')  
        form = LoginForm()
    return render(request, 'green_world/login.html', {'form': form, 'next': next_url})


# index
def index(request):
    categories = CategoryPlant.objects.all()
    return render(request, 'green_world/index.html', {'categories': categories})


# search_results
def search_results(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Plants_Types.objects.filter(name__icontains=query)
    return render(request, 'green_world/search_results.html', {
        'query': query,
        'results': results
    })

#favorites
def add_to_favorites(request, plant_id):
    plant = get_object_or_404(Plants_Types, pk=plant_id)
    
    if not request.user.is_authenticated:
        request.session['plant_to_save'] = plant_id
        return redirect(reverse('login') + '?next=' + request.path)
    FavoritePlant.objects.get_or_create(user=request.user, plant=plant)
    return redirect('favorites')


@login_required
def favorites(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to view your favorite plants.')
        return redirect(reverse('login') + '?next=' + request.path)

    favorites = FavoritePlant.objects.filter(user=request.user)
    if not favorites.exists():
        messages.info(request, 'You have no favorite plants yet.')
    return render(request, 'green_world/favorites.html', {'favorites': favorites})

@login_required
def remove_from_favorites(request, plant_id):
    plant = get_object_or_404(Plants_Types, pk=plant_id)
    favorite = FavoritePlant.objects.filter(user=request.user, plant=plant)
    if favorite.exists():
        favorite.delete()
        messages.success(request, 'Plant removed from favorites.')
    else:
        messages.error(request, 'Plant not in favorites.')
    return redirect('favorites')











