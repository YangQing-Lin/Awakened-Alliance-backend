from django.urls import path
from AwakenedAlliance.views import index

urlpatterns = [
    path("", index, name="index"),
]