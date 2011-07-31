from django.db import models

class FoodType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)
