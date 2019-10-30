from flask_restplus import fields
from extensions import api

requirements_serializer = api.model('Requirement', {
    "id_user": fields.Integer(required=True)
})
