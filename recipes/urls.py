from django.urls import path
from recipes.views import RecipeList, RegisterUser, LoginUser, CustomTokenRefreshView

urlpatterns = [
    path('api/recipes/', RecipeList.as_view(), name='recipe-list'),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/login/', LoginUser.as_view(), name='login'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
