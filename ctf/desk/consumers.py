import json
from django.core.cache import cache
from django.db.models import Sum, Max, Count
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from challenge.models import ChallengeSubmission
# from asgiref.sync import async_to_sync


class LeaderBoardWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("ctf_leaderboard_channel", self.channel_name)
        await self.accept()
        await self.send(json.dumps({"message": "connected successfully."}))
        await self.send(json.dumps({"score": await self.get_initial_data()}))
        

    async def disconnect(self, code):
        pass

    async def receive(self, text_data):
        pass

    async def send_message(self, event):
        # await print('sending msg', event)
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

    async def send_score(self, event):
        message, active = event["score"], event["active"]
        await self.send(text_data=json.dumps({"score": message, "active": active}))

    async def close_connection(self, event):
        await self.close()
    
    @database_sync_to_async
    def get_initial_data(self):
        data = ChallengeSubmission.objects.values(
            'contestant', 'contestant__first_name', 'contestant__last_name'
            ).annotate(
                points=Sum('challenge__points'), flags=Count('id'), last=Max('time')
            ).order_by('-points', 'last')
        return json.dumps(list(data))

