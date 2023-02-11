from django.http import JsonResponse
from AwakenedAlliance.models.player.player import Player


def getinfo_acapp(request):
    print("******")
    print("getinfo acapp")
    print("username:", user)
    print("********")
    player = Player.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'username': player.user.username,
        'photo': player.photo,
    })


def getinfo_web(request):
    # 判断是否登录
    user = request.user
    print("----------")
    print("getinfo web")
    print("username:", user)
    print(request)
    print("----------")
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录",
        })
    else:
        player = Player.objects.all()[0]
        return JsonResponse({
            'result': "success",
            'username': player.user.username,
            'photo': player.photo,
        })


def getinfo(request):
    platform = request.GET.get('platform')
    if platform == "ACAPP":
        return getinfo_acapp(request)
    else:
        return getinfo_web(request)