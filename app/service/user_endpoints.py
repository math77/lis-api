from flask import request
from flask_restplus import Resource
from extensions import api
from app.serializers.user_serializer import user_serializer
from app.controller.user_controller import UserController

namespace_user = api.namespace("user", description="Operations related with users")

@namespace_user.route("/")
class UserCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(UserCollection, self).__init__(api, args, kwargs)
        self.user = UserController()


    @api.expect(user_serializer)
    def post(self):
        data = request.json
        return self.user.add_user(email=data.get("email"), password=data.get("password"), cpf=data.get("cpf"))
