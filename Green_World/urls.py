from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_to_favorites/<int:plant_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:plant_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('plant_ai/', include('plant_ai.urls')),
]
