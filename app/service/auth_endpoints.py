from flask import request
from flask_restplus import Resource
from extensions import api
from chatbot.serializers.user_serializer import auth_serializer
from chatbot.controller.user_controller import AuthController

namespace_auth = api.namespace("auth", description="Operations related with authentication")


@namespace_auth.route("/login")
class UserLogin(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(UserLogin, self).__init__(api, args, kwargs)
        self.auth = AuthController()


    @api.expect(auth_serializer)
    def post(self):
        data = request.json
        return AuthController.login(data=data)