from .user_controller import UserController
from chatbot.helpful.tokens import encode_auth_token

class Auth:

    @staticmethod
    def login(data):
        try:
            user = UserController().login_user(cpf=data.get("cpf"), password=data.get("password"))
            if user:
                auth_token = encode_auth_token(user["id"])
                if auth_token:
                    response_object = {
                        "status": "success",
                        "message": "Loggedd Uu",
                        "Authorization": auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    "status": "fail",
                    "message": "Email or password does not match"
                }
                return response_object, 401

        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "Try again"
            }
            return response_object, 500


    @staticmethod
    def logout(data):
        pass
