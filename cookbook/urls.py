from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.urls import get_resolver
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('recipes.urls')),
    path('show-urls/', lambda request:
        JsonResponse({
            url.name or (url.pattern._route if hasattr(url.pattern, '_route') else 'Unnamed URL'):
            str(url.pattern)
            for url in get_resolver().url_patterns
            if hasattr(url, 'pattern')  # Filter out patterns without 'pattern'
        })
    ),
]
