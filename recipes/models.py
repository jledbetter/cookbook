from django.db import models
from django.contrib.auth.models import User

import datetime

class FoodType(models.Model):
    # always set a character length
    # blank = False and null = False make the field required
    name = models.CharField(max_length = 100, blank = False, null = False)
    
    def __unicode__(self):
        return '%s' % self.name
 
class Recipe(models.Model):
    title = models.CharField(max_length = 100, blank = False, null = False)
    # this is a many to many since a dish can have more than one food type
    food_type = models.ManyToManyField(FoodType)
    added_by = models.ForeignKey(User)
    # this tells the model to automatically timestamp it when it is added
    date_added = models.DateField(auto_now_add=True, default=datetime.datetime.now)
    instructions = models.TextField(max_length = 2000, blank = False, null = False)
    ingredients = models.TextField(max_length = 1000)
    
    def __unicode__(self):
        return '%s' % self.title