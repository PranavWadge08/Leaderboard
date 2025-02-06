import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def update_leaderboard(data, active):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("ctf_leaderboard_channel", {"type": "send.score", "score": json.dumps(list(data)), "active": json.dumps(active)})