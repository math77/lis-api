import bcrypt
from extensions import mongo


class UserController:

    def check_cpf_valid(self, cpf):
        return mongo.db.users.find_one({"cpf": cpf})


    def add_user(self, email, password, cpf):
        if self.check_cpf_valid(cpf):
            return False
        hashpass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return mongo.db.users.insert({"email": email, "password": hashpass, "cpf": cpf})


    @staticmethod
    def login_user(cpf, password):
        user = mongo.db.users.find_one({"cpf": cpf})
        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user["password"]):
                return user


    @staticmethod
    def check_auth_token(self, auth_token):
        return mongo.db.users.find_one({"auth_token": auth_token})


    @staticmethod
    def save_auth_token(id_user, auth_token):
        if auth_token:
            return mongo.db.users.update_one({"_id": id_user}, { "$set": {"auth_token": auth_token}})
