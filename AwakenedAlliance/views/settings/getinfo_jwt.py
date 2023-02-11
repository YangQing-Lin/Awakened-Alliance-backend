from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from AwakenedAlliance.models.player.player import Player


class InfoView(APIView):
    permission_classes = ([IsAuthenticated])
    print("IIIIIIIIIII")

    def get(self, request):
        print("###########")
        print("获取令牌:", request)
        print("###########")
        user = request.user
        player = Player.objects.get(user=user)
        return Response({
            'result': "success",
            'username': user.username,
            'photo': player.photo,
        })