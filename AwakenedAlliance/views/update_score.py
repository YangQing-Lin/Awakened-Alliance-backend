from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from AwakenedAlliance.models.player.player import Player


class UpdateScoreView(APIView):
    # 权限(Permission)的校验发生验证用户身份以后，是由系统根据分配权限确定用户可以访问何种资源以及对这种资源进行何种操作，这个过程也被称为授权(Authorization)。
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        score = int(request.POST.get('rank_score', 0))
        game_mode = str(request.POST.get('game_mode', ""))
        if game_mode == "single mode":
            return self.update_single_mode_score(request, score)
        elif game_mode == "multi mode":
            return self.update_rank_score(request, score)
    
    
    def update_single_mode_score(self, request, single_mode_score):
        print("SINGLE MODE SCORE: ", single_mode_score)
        if  single_mode_score < 0:
            return Response({
                'result': "single_mode_score参数不合法"
            })
        player = Player.objects.get(user=request.user)
        player.single_mode_score = max(player.single_mode_score, single_mode_score)
        player.save()
        return Response({
            'result': "success",
        })


    def update_rank_score(self, request, rank_score):
        print("MULTI MODE SCORE: ", rank_score)
        if  rank_score < 0:
            return Response({
                'result': "rank_score参数不合法"
            })
        player = Player.objects.get(user=request.user)
        player.rank_score = max(player.rank_score, rank_score)
        player.save()
        return Response({
            'result': "success",
        })