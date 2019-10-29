from extensions import mongo


class ChatController:

    def add_message(self, message_data):
        mongo.db.messages.add.insert_one(message_data)


    def get_messages_chat(self, id_chat):
        return mongo.db.messages.find({"id_chat":id_chat})
