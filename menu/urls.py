from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from dishes.views import DishViewSet, DrinkViewSet, IngredientViewSet, DessertViewSet

router = routers.DefaultRouter()
router.register(r'dishes', DishViewSet, basename='dish')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'drinks', DrinkViewSet, basename='drink')
router.register(r'desserts', DessertViewSet, basename='dessert')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/', RedirectView.as_view(url='/admin/logout')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls)
]