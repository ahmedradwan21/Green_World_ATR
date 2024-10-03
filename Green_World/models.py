from django.db import models
from django.contrib.auth.models import User
from plants.models import Plants_Types 

class FavoritePlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plants_Types, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'plant')
    
    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"
