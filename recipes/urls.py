from django.urls import path
from .views import RecipeList

urlpatterns = [
    path('api/recipes/', RecipeList.as_view(), name='recipe-list'),
]
