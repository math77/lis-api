from flask import request
from flask_restplus import Resource
from bson.objectid import ObjectId
from extensions import api
from app.schemas import RequirementSchema
from app.helpful.status import StatusRequirement
from app.serializers.requirements_serializer import requirements_serializer
from app.controller.requirements_controller import RequirementsController


namespace_requirements = api.namespace("requirements", description="Operations related with requirements")


@namespace_requirements.route("/")
class RequirementsCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(RequirementsCollection, self).__init__(api, args, kwargs)
        self.requirements = RequirementsController()


    @api.expect(requirements_serializer)
    def post(self):
        data = request.json
        #representa o primeiro status de uma solicitação que é o de "solicitada"
        status = StatusRequirement.REQUESTED.value
        id_user = ObjectId(data.get("id_user"))
        return self.requirements.save_basic_requirement(id_user=id_user, status=status)


    def get(self):
        schema = RequirementSchema(many=True)
        data = self.requirements.get_requirements()
        return schema.dump(data)


@namespace_requirements.route("/<id>")
class RequirementsDetail(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(RequirementsDetail, self).__init__(api, args, kwargs)
        self.requirements = RequirementsController()


    @api.expect(requirements_serializer)
    def put(self, id):
        value_id = ObjectId(id)
        data = request.json

        #id_requirement = data.get("id")
        lane_number = data.get("lane_number")
        front_img_doc_responsible = data.get("front_img_doc_responsible")
        verse_img_doc_responsible = data.get("verse_img_doc_responsible")
        img_birth_certificate = data.get("img_birth_certificate")
        img_selfie_user = data.get("img_selfie_user")
        doc_pickup_address = data.get("doc_pickup_address")

        return self.requirements.update_requirement_rg(id=ObjectId(value_id),
                                                       lane_number=lane_number,
                                                       front_img_doc_responsible=front_img_doc_responsible,
                                                       verse_img_doc_responsible=verse_img_doc_responsible,
                                                       img_birth_certificate=img_birth_certificate,
                                                       img_selfie_user=img_selfie_user,
                                                       doc_pickup_address=doc_pickup_address)
