from .user_controller import UserController
from app.helpful.tokens import encode_auth_token

class AuthController:

    def login(self, data):
        try:
            user = UserController().login_user(cpf=data.get("cpf"), password=data.get("password"))
            if user:
                auth_token = encode_auth_token(user["_id"])
                saved = UserController().save_auth_token(user["_id"], auth_token)
                if saved:
                    response_object = {
                        "status": "success",
                        "message": "Loggedd Uu",
                        "Authorization": auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    "status": "fail",
                    "message": "CPF or password does not match"
                }
                return response_object, 401

        except Exception as e:
            response_object = {
                "exception": str(e),
                "status": "fail",
                "message": "Try again"
            }
            return response_object, 500


    @staticmethod
    def logout(data):
        pass
