from django.urls import path
from AwakenedAlliance.views.settings.getinfo import getinfo
from AwakenedAlliance.views.settings.login import signin
from AwakenedAlliance.views.settings.logout import signout


urlpatterns = [
    path("getinfo/", getinfo, name="settings_getinfo"),
    path("login/", signin, name="login"),
    path("logout/", signout, name="logout"),
]
