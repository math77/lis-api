from flask_restplus import Api
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow


api = Api(version="beta", title="Lis API", description="Beta API of Lis")
mongo = PyMongo()
mars = Marshmallow()
bcrypt = Bcrypt()
