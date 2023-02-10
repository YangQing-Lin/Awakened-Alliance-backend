from django.urls import path
from AwakenedAlliance.views.settings.getinfo import getinfo
from AwakenedAlliance.views.settings.login import signin
from AwakenedAlliance.views.settings.logout import signout
from AwakenedAlliance.views.settings.register import register


urlpatterns = [
    path("getinfo/", getinfo, name="settings_getinfo"),
    path("login/", signin, name="settings_login"),
    path("logout/", signout, name="settings_logout"),
    path("register/", register, name="settings_register"),
]
