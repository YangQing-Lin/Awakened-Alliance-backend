from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from AwakenedAlliance.models.player.player import Player


class GetRankListView(APIView):
    # 权限(Permission)的校验发生验证用户身份以后，是由系统根据分配权限确定用户可以访问何种资源以及对这种资源进行何种操作，这个过程也被称为授权(Authorization)。
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        select_type = request.GET.get('select_type', 0)
        res = {'me': "res test"}
        if select_type == "rank score":
            res = self.get_rank_list(request)
            # me = Player.objects.get(user=request.user)
            # res = {
            #     'me': {
            #         'username': me.user.username,
            #         'photo': me.photo,
            #         'score': me.rank_score,
            #         'rank': Player.objects.filter(rank_score__gt=me.rank_score).count() + 1,
            #     },
            #     'all': [],
            # }

            # players = Player.objects.all().order_by('-rank_score')[:10]
            # for player in players:
            #     res['all'].append({
            #         'username': player.user.username,
            #         'photo': player.photo,
            #         'score': player.rank_score,
            #         'rank': Player.objects.filter(rank_score__gt=player.rank_score).count() + 1,
            #     })

            # return Response(res)
        elif select_type == "single mode score":
            res = self.get_single_mode_list(request)

        return Response(res)


    def get_single_mode_list(self, request):
        # 没有登录可以用user_id=1强制搜索第一个用户，user=request.user就指的是登录的用户
        me = Player.objects.get(user=request.user)
        res = {
            'me': {
                'username': me.user.username,
                'photo': me.photo,
                'score': me.single_mode_score,
                'rank': Player.objects.filter(single_mode_score__gt=me.single_mode_score).count() + 1,
            },
            'all': [],
        }

        players = Player.objects.all().order_by('-single_mode_score')[:10]
        for player in players:
            res['all'].append({
                'username': player.user.username,
                'photo': player.photo,
                'score': player.single_mode_score,
                'rank': Player.objects.filter(single_mode_score__gt=player.single_mode_score).count() + 1,
            })

        return res
    

    def get_rank_list(self, request):
        # 没有登录可以用user_id=1强制搜索第一个用户，user=request.user就指的是登录的用户
        me = Player.objects.get(user=request.user)
        res = {
            'me': {
                'username': me.user.username,
                'photo': me.photo,
                'score': me.rank_score,
                'rank': Player.objects.filter(rank_score__gt=me.rank_score).count() + 1,
            },
            'all': [],
        }

        players = Player.objects.all().order_by('-rank_score')[:10]
        for player in players:
            res['all'].append({
                'username': player.user.username,
                'photo': player.photo,
                'score': player.rank_score,
                'rank': Player.objects.filter(rank_score__gt=player.rank_score).count() + 1,
            })

        return res