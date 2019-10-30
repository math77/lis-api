import datetime
from extensions import mongo


class RequirementsController:

    def save_requirement(self, id_user, status):
        date = datetime.datetime.now()
        return mongo.db.requirements.insert({"id_user": id_user, "status": status, "date": date})


    def update_requirement(self, id):
        #return mongo.db.requirements.update_one({"_id": id})
        pass

    #pegar os requerimentos com base no endereço do SAC escolhido.
    def get_requirements(self, data):
        pass
