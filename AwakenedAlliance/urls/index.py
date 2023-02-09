from django.urls import path, include
from AwakenedAlliance.views.index import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", index, name="index"),
    path("menu/", include("AwakenedAlliance.urls.menu.index")),
    path("playground/", include("AwakenedAlliance.urls.playground.index")),
    path("settings/", include("AwakenedAlliance.urls.settings.index")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
