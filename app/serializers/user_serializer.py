from flask_restplus import fields
from extensions import api

user_serializer = api.Model('User', {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "cpf": fields.String(required=True),
    "first_name": fields.String()
})

auth_serializer = api.Model('Auth', {
    "cpf": fields.String(required=True),
    "password": fields.String(required=True)
})
