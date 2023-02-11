from django.urls import path
from AwakenedAlliance.views.settings.getinfo import getinfo
from AwakenedAlliance.views.settings.getinfo_jwt import InfoView
from AwakenedAlliance.views.settings.login import signin
from AwakenedAlliance.views.settings.logout import signout
from AwakenedAlliance.views.settings.register import register


# 有了jwt验证之后，login可以删掉了
# 因为jwt登录实际上是把登录信息存在Client端
# 所以登出只需要在Client端删除信息即可，不需要给后端发请求
# logout也可以删掉
# 这里不删是为了以后其他项目可能还要用的这种登录验证方式
urlpatterns = [
    path("getinfo/", getinfo, name="settings_getinfo"),
    path("getinfo_jwt/", InfoView.as_view(), name="settings_getinfo"),
    path("login/", signin, name="settings_login"),
    path("logout/", signout, name="settings_logout"),
    path("register/", register, name="settings_register"),
]
