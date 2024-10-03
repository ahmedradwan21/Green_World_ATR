from django.db import models
# Create your models here.
class CategoryPlant(models.Model):
    x = [
        ('Vegetables','Vegetables'),
        ('Leaf Plants','Leaf Plants'),
        ('Flowers','Flowers'),
        ('Fruits','Fruits'),
        ('Succulents','Succulents'),
        ('Weeds','Weeds'),
        ('Trees','Trees'),
        ('Toxic Plants','Toxic Plants'),
    ]
    name = models.CharField(max_length=100, null=True, blank=True, choices=x)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Plants_Types(models.Model):
    name = models.CharField(max_length=100, verbose_name='common_name')
    scientific_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    descriptions = models.TextField()
    plant_origin = models.TextField(null=True, blank=True)
    category = models.ForeignKey(CategoryPlant, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'plant' 

class Scientific_Classification(models.Model):
    plant_type = models.OneToOneField(Plants_Types, on_delete=models.CASCADE, null=True, blank=True)
    phylum = models.CharField(max_length=100, null=True, blank=True)
    Class = models.CharField(max_length=100, null=True, blank=True)
    order = models.CharField(max_length=100, null=True, blank=True)
    family = models.CharField(max_length=100, null=True, blank=True)
    genus = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)
    


class Care_Guide(models.Model):
    plant_type = models.OneToOneField(Plants_Types, on_delete=models.CASCADE, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    watering_care = models.TextField(null=True, blank=True)
    fertilizing_care = models.TextField(null=True, blank=True)
    pruning = models.TextField(null=True, blank=True)
    soil_care = models.TextField(null=True, blank=True)
    sun_light = models.TextField(null=True, blank=True)
    IdealTemperature = models.TextField(null=True, blank=True)
    Propagation = models.TextField(null=True, blank=True)
    TransplantingTime = models.TextField(null=True, blank=True)
    PlantingTime = models.TextField(null=True, blank=True)
    HarvestTime = models.TextField(null=True, blank=True)

class Attributes(models.Model):
    plant_type = models.OneToOneField(Plants_Types, on_delete=models.CASCADE, null=True, blank=True)
    Lifespan = models.CharField(max_length=100, null=True, blank=True)
    Plant_Type = models.CharField(max_length=200, null=True, blank=True)
    Planting_Time = models.CharField(max_length=100, null=True, blank=True)
    Bloom_Time = models.CharField(max_length=200, null=True, blank=True)
    Harvest_Time = models.CharField(max_length=200, null=True, blank=True)
    Plant_Height = models.CharField(max_length=100, null=True, blank=True)
    Spread = models.CharField(max_length=50, null=True, blank=True)
    Flower_Size = models.CharField(max_length=100, null=True, blank=True)
    Dormancy = models.CharField(max_length=100, null=True, blank=True)
    Leaf_type = models.CharField(max_length=100, null=True, blank=True)
    Ideal_Temperature = models.CharField(max_length=100, null=True, blank=True)
    Pollinators = models.CharField(max_length=100, null=True, blank=True)
    Growth_Rate = models.CharField(max_length=100, null=True, blank=True)
    Water = models.CharField(max_length=100, null=True, blank=True)
    Sunlight = models.CharField(max_length=100,null=True, blank=True)
    
    

