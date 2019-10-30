from flask_restplus import fields
from extensions import api

user_serializer = api.model('User', {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "cpf": fields.String(required=True),
    "first_name": fields.String()
})

auth_serializer = api.model('Auth', {
    "cpf": fields.String(required=True),
    "password": fields.String(required=True)
})
