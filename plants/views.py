from django.shortcuts import render, get_object_or_404
from .models import Plants_Types, CategoryPlant, Scientific_Classification, Care_Guide, Attributes
import requests

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plants_Types, pk=plant_id)
    classification = Scientific_Classification.objects.filter(plant_type=plant).first()
    care_guide = Care_Guide.objects.filter(plant_type=plant).first()
    attributes = Attributes.objects.filter(plant_type=plant).first()
    return render(request, 'plants/plant_detail.html', {'plant': plant,'classification': classification,
        'care_guide': care_guide,
        'attributes': attributes})

def plants_by_category(request, category_id):
    category = get_object_or_404(CategoryPlant, pk=category_id)
    plants = Plants_Types.objects.filter(category=category)
    return render(request, 'plants/category_plants.html', {'category': category, 'plants': plants,})
    

def upload_image(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        response = requests.post('http://localhost:5000/predict', files={'file': file})
        if response.status_code == 200:
            result = response.json().get('prediction', 'Error: No prediction found')
        else:
            result = f'Error: {response.status_code} - {response.text}'
        return render(request, 'prediction/upload.html', {'result': result})
    return render(request, 'prediction/upload.html')