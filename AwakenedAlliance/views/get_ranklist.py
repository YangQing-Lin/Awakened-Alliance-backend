from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from AwakenedAlliance.models.player.player import Player


class GetRankListView(APIView):
    # permission_classes = ([IsAuthenticated])

    def get(self, request):
        # 如果没有登陆就一直把id=1的用户当成自己
        me = Player.objects.get(user_id=1)
        res = {
            'me': {
                'username': me.user.username,
                'photo': me.photo,
                'score': me.score,
                'rank': Player.objects.filter(score__gt=me.score).count() + 1,
            },
            'all': [],
        }

        players = Player.objects.all().order_by('-score')[:10]
        for player in players:
            res['all'].append({
                'username': player.user.username,
                'photo': player.photo,
                'score': player.score,
                'rank': Player.objects.filter(score__gt=player.score).count() + 1,
            })

        return Response(res)