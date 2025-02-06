from django.urls import path
from .views import (HomeView, FlagSubmitView, LeaderBoardView, ScoreView)

app_name = "desk"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('score/', ScoreView.as_view(), name='score'),
    path('submit-flag/', FlagSubmitView.as_view(), name='submit_flag'),
    path('leaderboard/', LeaderBoardView.as_view(), name='leaderboard'),
]
