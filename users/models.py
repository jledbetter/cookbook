from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=255, default='', unique=True)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=255, default='')
    bio = models.TextField()
    food_type = models.ManyToManyField(FoodType)

