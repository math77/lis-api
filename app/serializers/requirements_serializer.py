from flask_restplus import fields
from extensions import api

requirements_serializer = api.model('Requirement', {
    "id_user": fields.String(),
    "lane_number": fields.Integer(),
    "front_img_doc_responsible": fields.String(),
    "verse_img_doc_responsible": fields.String(),
    "img_birth_certificate": fields.String(),
    "img_selfie_user": fields.String(),
    "doc_pickup_address": fields.String()
})
