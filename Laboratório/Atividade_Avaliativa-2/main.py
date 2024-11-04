from query import Database
from teacher_crud import TeacherCRUD

database = Database("bolt://52.90.188.40", "neo4j", "servo-piles-battleships")
crud = TeacherCRUD(database)

# Questão 3
crud.create("Chris Lima", 1956, "189.052.396-66")

print("Lendo Teacher com nome 'Chris Lima':")
print(crud.read("Chris Lima"))

crud.update("Chris Lima", "162.052.777-77")

print("Lendo Teacher com nome 'Chris Lima' alterado:")
print(crud.read("Chris Lima"))


crud.delete("Chris Lima")

database.close()
