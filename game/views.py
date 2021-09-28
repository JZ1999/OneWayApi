from rest_framework import viewsets

from game.models import LeaderBoardEntry
from game.serializers import LeaderBoardsSerializer


class OfflineLeaderBoardView(viewsets.ModelViewSet):
    queryset = LeaderBoardEntry.objects.filter(account__banned=False).order_by("offline")
    serializer_class = LeaderBoardsSerializer

