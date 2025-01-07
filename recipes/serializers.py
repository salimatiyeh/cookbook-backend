from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(
        many=True,
        queryset=Ingredient.objects.all(),
        slug_field='name'  # Show ingredient name instead of ID
    )

# class RecipeSerializer(serializers.ModelSerializer):
#     ingredients = serializers.PrimaryKeyRelatedField(
#         queryset=Ingredient.objects.all(),
#         many=True
#     )
    class Meta:
        model = Recipe
        fields = '__all__'
