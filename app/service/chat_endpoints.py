from flask_restplus import Resource
from extensions import api
from app.serializers.chat_serializer import message_serializer
from app.controller.chat_controller import ChatController


namespace_chat = api.namespace("chat", description="Operations related with chat")


@namespace_chat.route("/")
class ChatCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(ChatCollection, self).__init__(api, args, kwargs)
        self.chat = ChatController()

    @api.expect(message_serializer)
    def post(self):
        return self.chat.add_message(api.payload)
