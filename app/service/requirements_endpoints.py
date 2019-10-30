from flask import request
from flask_restplus import Resource
from extensions import api
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
        return self.requirements.save_requirement(id_user=data.get("id_user"), status=status)
