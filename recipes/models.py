from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=110)
    ingredients = models.TextField()
    instructions = models.TextField()
    creator = models.ForeignKey(User)
    food_type = models.ManyToManyField(FoodType)
    created_on = models.DateTimeField(
        auto_now_add=True, default=datetime.datetime.now)