from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from AwakenedAlliance.models.player.player import Player


class UpdateScoreView(APIView):
    # 权限(Permission)的校验发生验证用户身份以后，是由系统根据分配权限确定用户可以访问何种资源以及对这种资源进行何种操作，这个过程也被称为授权(Authorization)。
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        score = int(request.POST.get('score', 0))
        if  score < 0:
            return Response({
                'result': "score参数不合法"
            })
        player = Player.objects.get(user=request.user)
        player.score = max(player.score, score)
        player.save()
        return Response({
            'result': "success",
        })