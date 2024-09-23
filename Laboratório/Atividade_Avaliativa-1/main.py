from database import Database
from motorista_model import motorista_model
from motoristaDAO import MotoristaDAO

db = Database(database="atividade_avaliativa", collection="Motoristas")
motorista_model = motorista_model(database=db)


motorista = MotoristaDAO(motorista_model)
motorista.run()