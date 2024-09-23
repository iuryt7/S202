from pymongo import MongoClient
from bson.objectid import ObjectId

class motorista_model:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista_id, nome, corridas, nota):
        try:
            res = self.db.collection.insert_one({
                'motorista_id': motorista_id,
                'nome': nome,
                'corridas': corridas,
                'nota': nota
            })
            print("Motorista criado com sucesso!")
            return res.inserted_id
        except Exception as e:
            print("Motorista não foi criado. Erro: ", e)
            return None
    
    def read_motorista(self, motorista_id):
        try:
            res = self.db.collection.find_one({'motorista_id': motorista_id})
            print(f"Motorista encontrado com sucesso! { res}")
            return res
        except Exception as e:
            print("Motorista não foi encontrado. Erro: ", e)
            return None
        
    def update_motorista(self, motorista_id, nome, corridas, nota):
        try:
            res = self.db.collection.update_one(
                {'motorista_id': motorista_id},
                {'$set': {
                    'nome': nome,
                    'corridas': corridas,
                    'nota': nota
                }}
            )
            print("Motorista atualizado com sucesso!")
            return res.modified_count
        except Exception as e:
            print("Motorista não foi atualizado. Erro: ", e)
            return None
        
    def delete_motorista(self, motorista_id):
        try:
            res = self.db.collection.delete_one({'motorista_id': motorista_id})
            print("Motorista deletado com sucesso!")
            return res.deleted_count
        except Exception as e:
            print("Motorista não foi deletado. Erro: ", e)
            return None