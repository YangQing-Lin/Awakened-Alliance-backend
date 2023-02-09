from django.urls import path, include
from AwakenedAlliance.views.index import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from AwakenedAlliance.views.apply_code import apply_code
from AwakenedAlliance.views.receive_code import receive_code

urlpatterns = [
    path("", index, name="index"),
    path("menu/", include("AwakenedAlliance.urls.menu.index")),
    path("playground/", include("AwakenedAlliance.urls.playground.index")),
    path("settings/", include("AwakenedAlliance.urls.settings.index")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('apply_code/', apply_code, name='apply_code'),
    path('receive_code/', receive_code, name='receive_code'),
]
