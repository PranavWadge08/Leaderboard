from django.urls import path
from .consumers import LeaderBoardWebSocketConsumer


websocket_urlpatterns = [
    path('ws/ctf/leaderboard',
         LeaderBoardWebSocketConsumer.as_asgi()),
]
