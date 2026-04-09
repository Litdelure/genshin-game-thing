from django.db import models

# Create your models here.
class Player(models.Model):
    health=models.IntegerField(default=100)
    attack=models.IntegerField(default=100)
    speed=models.IntegerField(default=100)
    statMultiplier=models.IntegerField(default=1)
    



