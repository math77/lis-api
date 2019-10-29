import datetime
import jwt
from chatbot.controller.user_controller import UserController
from config import key


def encode_auth_token(id_user):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            "iat": datetime.datetime.utcnow(),
            "sub": id_user
        }
        return jwt.encode(
            payload,
            key,
            algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, key)
        valid_token = UserController().check_auth_token(auth_token=auth_token)
        if valid_token:
            return payload["sub"]
        else:
            return "Token invalid, please log in again"
    except jwt.ExpiredSignatureError:
        return "Signatue invalid, please log in again"
    except jwt.InvalidTokenError:
        return "Invalid token, please log in again"
