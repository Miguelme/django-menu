from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from dishes.models import Dish, Ingredient, Drink, Desert
from dishes.serializers import DishSerializer, IngredientSerializer, DrinkSerializer, DesertSerializer


class DishViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class IngredientViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class DrinkViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


class DesertViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = DesertSerializer
    queryset = Desert.objects.all()