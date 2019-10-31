from bson import ObjectId
from marshmallow import fields
from extensions import mars

class UserSchema(mars.Schema):
    class Meta:
        fields = ("email", "cpf", "password", "first_name",)


class MessageSchema(mars.Schema):
    class Meta:
        fields = ("message", "id_user", "id_bot", "date", "id_chat",)


class RequirementSchema(mars.Schema):
    class Meta:
        fields = ("lane_number", "id_user",)


# "Orientar" o marshmallow em como deve converter um ObjectId do mongo para String
# para que possa ser serializado para Json, pois Json não serializa ObjectId
mars.Schema.TYPE_MAPPING[ObjectId] = fields.String
