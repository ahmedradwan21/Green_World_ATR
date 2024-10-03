from django.urls import path
from . import views

urlpatterns = [
    path('plant/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('category/<int:category_id>/', views.plants_by_category, name='plants_by_category'),
    path('upload_image', views.upload_image, name='upload_image'),
]