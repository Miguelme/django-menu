from django.contrib import admin

from dishes.models import Drink, Dessert, Dish, Ingredient

admin.site.register(Drink)
admin.site.register(Dessert)
admin.site.register(Dish)
admin.site.register(Ingredient)
