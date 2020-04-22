from django.contrib import admin

from dishes.models import Drink, Desert, Dish, Ingredient

admin.site.register(Drink)
admin.site.register(Desert)
admin.site.register(Dish)
admin.site.register(Ingredient)