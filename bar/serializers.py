from rest_framework import serializers
from .models import AlcoholicDrink, Cocktail

class TypeOfDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlcoholicDrink
        fields = '__all__'

class CocktailSerializer(serializers.ModelSerializer):
    type = TypeOfDrinkSerializer()

    class Meta:
        model = Cocktail
        fields = '__all__'