from django.urls import path
from game.views import OfflineLeaderBoardView

urlpatterns = [
    path('leaderboard/offline/', OfflineLeaderBoardView.as_view({"get": "list", "post": "create"})),
]
