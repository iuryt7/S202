from pymongo import MongoClient
from bson.objectid import ObjectId

class BookModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, _id: int, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.insert_one({
                "_id": _id,
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            })
            print(f"Livro criado com o ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Um problema aconteceu tentando encontrar: {e}")
            return None

    def read_book_by_id(self, _id: int):
        try:
            res = self.db.collection.find_one({"_id": _id})
            if res:
                print(f"Livro nao encontrado: {res}")
            else:
                print("Livro nao encontrado.")
            return res
        except Exception as e:
            print(f"Um problema aconteceu tentando encontrar: {e}")
            return None

    def update_book(self, _id: int, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one(
                {"_id": _id},
                {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}}
            )
            print(f"Livro atualizado: {res.modified_count} documentos modificados")
            return res.modified_count
        except Exception as e:
            print(f"Um problema aconteceu tentando encontrar: {e}")
            return None

    def delete_book(self, _id: int):
        try:
            res = self.db.collection.delete_one({"_id": _id})  # Usando _id como inteiro
            print(f"Livro deletado: {res.deleted_count}")
            return res.deleted_count
        except Exception as e:
            print(f"Um problema aconteceu tentando encontrar: {e}")
            return None
