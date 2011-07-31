from django.contrib import admin
 
# import your models here
# for convenience I put all the models into one admin.py file
from recipes.models import FoodType, Recipe
from accounts.models import UserProfile
 
# creating a list of the models since the register() function
# won't take all of them as arguments
registered_models = [FoodType, Recipe, UserProfile]
admin.site.register(registered_models)