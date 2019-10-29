from marshmallow import fields
from extensions import mars

class UserSchema(mars.Schema):
    class Meta:
        fields = ("email", "cpf", "password", "first_name")


class MessageSchema(mars.Schema):
    class Meta:
        fields = ("message", "id_user", "id_bot", "date", "id_chat")
