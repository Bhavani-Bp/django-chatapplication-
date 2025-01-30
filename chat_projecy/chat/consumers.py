import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            # Add this WebSocket connection to the room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)

            await self.accept()  # Accept the WebSocket connection
        except Exception as e:
            print(f"Error in connect: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        except Exception as e:
            print(f"Error in disconnect: {e}")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data['message']
            sender = self.scope['user'].username  # Get the sender's username

            # Broadcast the message to all users in the room
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message, "sender": sender}
            )
        except Exception as e:
            print(f"Error in receive: {e}")

    async def chat_message(self, event):
        # Send the received message to the WebSocket client
        await self.send(text_data=json.dumps(event))
