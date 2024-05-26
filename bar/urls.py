from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CocktailListView

router = DefaultRouter()
router.register('post', CocktailListView)

urlpatterns = [
    path('', include(router.urls))
]