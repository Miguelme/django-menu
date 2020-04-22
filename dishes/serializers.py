from rest_framework import serializers

from dishes.models import Dish, Desert, Drink, Ingredient


class SimpleIngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingredient
		fields = ["name", "imageUrl"]


class DishSerializer(serializers.ModelSerializer):
	ingredients = SimpleIngredientSerializer(read_only=True, many=True)
	class Meta:
		model = Dish
		fields = '__all__'


class DesertSerializer(serializers.ModelSerializer):
	ingredients = SimpleIngredientSerializer(read_only=True, many=True)
	class Meta:
		model = Desert
		fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):
	ingredients = SimpleIngredientSerializer(read_only=True, many=True)
	class Meta:
		model = Drink
		fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
	ingredients = SimpleIngredientSerializer(read_only=True, many=True)
	class Meta:
		model = Ingredient
		fields = '__all__'
