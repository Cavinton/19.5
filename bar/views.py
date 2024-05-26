from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet


# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import AlcoholicDrink, Cocktail
from .serializers import TypeOfDrinkSerializer, CocktailSerializer

class TypeOfDrinkListView(ModelViewSet):
    queryset = AlcoholicDrink.objects.all()
    serializer_class = TypeOfDrinkSerializer

class CocktailListView(ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

# @api_view(['GET'])
# def expensive_drink(request):
#     return Cocktail.objects.filter()
