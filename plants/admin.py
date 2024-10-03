from django.contrib import admin
# Register your models here.
from .models import Plants_Types, Scientific_Classification, Care_Guide, Attributes, CategoryPlant
@admin.register(CategoryPlant)
class CategoryPlantAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Plants_Types)
class PlantsTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')

@admin.register(Scientific_Classification)
class ScientificClassificationAdmin(admin.ModelAdmin):
    list_display = ('plant_type', 'family', 'genus', 'species')

@admin.register(Care_Guide)
class CareGuideAdmin(admin.ModelAdmin):
    list_display = ['plant_type']

@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ['plant_type', 'Lifespan', 'Plant_Type']