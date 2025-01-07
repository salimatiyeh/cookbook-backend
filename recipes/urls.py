from django.urls import path
from recipes.views import RecipeList, RegisterUser, LoginUser, CustomTokenRefreshView, RecipeDetail, IngredientCreate, IngredientList

urlpatterns = [
    path('api/recipes/', RecipeList.as_view(), name='recipe-list'),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/login/', LoginUser.as_view(), name='login'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/recipes/<int:id>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('api/recipes/<int:id>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('api/ingredients/', IngredientCreate.as_view(), name='ingredient-list'),
    path('api/ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('api/recipes/', RecipeList.as_view(), name='recipe-list'),
    path('api/recipes/<int:id>/', RecipeDetail.as_view(), name='recipe-detail'),
]
