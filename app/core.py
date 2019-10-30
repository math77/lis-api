from flask import Flask, Blueprint
from config import Config
from extensions import api, mongo, mars
from app.helpful.encoder_custom import JSONEncoder
from app.service.chat_endpoints import namespace_chat
from app.service.user_endpoints import namespace_user
from app.service.auth_endpoints import namespace_auth
from app.service.requirements_endpoints import namespace_requirements

import json
import datetime
from bson import ObjectId


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    blueprint = Blueprint("api", __name__)

    #app.register_blueprint(blueprint)

    api.init_app(blueprint)
    app.register_blueprint(blueprint)
    mars.init_app(app)
    mongo.init_app(app)
    #bcrypt.init_app(app)

    api.add_namespace(namespace_chat)
    api.add_namespace(namespace_auth)
    api.add_namespace(namespace_user)
    api.add_namespace(namespace_requirements)

    app.json_encoder = JSONEncoder

    return app
