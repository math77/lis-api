from flask_restplus import fields
from extensions import api

message_serializer = api.model('Message', {
    "message": fields.String(required=True, description="Message text send"),
    "id_user": fields.Integer(),
    "id_bot": fields.Integer(),
    "id_chat": fields.Integer(required=True),
    "date":  fields.DateTime(dt_format="iso8601")
})
