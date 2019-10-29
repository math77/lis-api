from flask import Flask, Blueprint
from config import Config
from extensions import api, mongo, mars, bcrypt
from chatbot.service.chat_endpoints import namespace_chat, namespace_auth, namespace_user

app = Flask(__name__)


def create_app():
    app.config.from_object(Config)

    blueprint = Blueprint("api", __name__)

    #app.register_blueprint(blueprint)

    api.init_app(blueprint)
    app.register_blueprint(blueprint)
    mars.init_app(app)
    mongo.init_app(app)
    bcrypt.init_app(app)

    api.add_namespace(namespace_chat)
    api.add_namespace(namespace_auth)
    api.add_namespace(namespace_user)


def main():
    create_app(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()
