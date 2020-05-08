from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import routers

from dishes.views import DishViewSet, DrinkViewSet, IngredientViewSet, DesertViewSet

router = routers.DefaultRouter()
router.register(r'dishes', DishViewSet, basename='dish')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'drinks', DrinkViewSet, basename='drink')
router.register(r'desert', DesertViewSet, basename='desert')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/', RedirectView.as_view(url='/admin/logout')),
    path('admin/', admin.site.urls)
]