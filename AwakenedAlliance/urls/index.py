from django.urls import path, include
from AwakenedAlliance.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("menu/", include("AwakenedAlliance.urls.menu.index")),
    path("playground/", include("AwakenedAlliance.urls.playground.index")),
    path("settings/", include("AwakenedAlliance.urls.settings.index")),
]
