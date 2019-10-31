import datetime
import pymongo
from pymongo import errors
from extensions import mongo


class RequirementsController:

    def save_basic_requirement(self, id_user, status):
        date = datetime.datetime.now()
        return mongo.db.requirements.insert({"id_user": id_user, "status": status, "date": date})


    #Responsável por salvar as informações de um RG no requerimento.
    def update_requirement_rg(self, id, lane_number=None, front_img_doc_responsible=None,
                              verse_img_doc_responsible=None, img_birth_certificate=None,
                              img_selfie_user=None, doc_pickup_address=None):
        query = {"_id": id}

        values2 = {"$set": {"infos_rg.lane_number": lane_number,
                          "infos_rg.front_img_doc_responsible": front_img_doc_responsible,
                          "infos_rg.verse_img_doc_responsible": verse_img_doc_responsible,
                          "infos_rg.img_birth_certificate": img_birth_certificate,
                          "infos_rg.img_selfie_user": img_selfie_user,
                          "infos_rg.doc_pickup_address": doc_pickup_address}}

        values = { "$set": {"infos_rg": {"lane_number": lane_number,
                  "front_img_doc_responsible": front_img_doc_responsible,
                  "verse_img_doc_responsible": verse_img_doc_responsible,
                  "img_birth_certificate": img_birth_certificate,
                  "img_selfie_user": img_selfie_user,
                  "doc_pickup_address": doc_pickup_address}}}

        try:
            result = mongo.db.requirements.update_one(query, values2)
            if result:
                return "Atualizouuu"
        except pymongo.errors.OperationFailure as e:
            print("ERRO AQUIIIII")
            print(str(e))
            return str(e)
        return "Algum errroo"

    #pegar os requerimentos com base no endereço do SAC escolhido.
    def get_requirements(self):
        return mongo.db.requirements.find()
