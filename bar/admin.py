from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AlcoholicDrink, Cocktail

admin.site.register(AlcoholicDrink)
admin.site.register(Cocktail)
# admin.site.register(LimitedSet)