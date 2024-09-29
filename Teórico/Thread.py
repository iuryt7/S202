import random
import time
from pymongo import collection
class sensores:
    def __init__(self,database):
        self.database = database

    def sensor(self, nome, intervalo):
        while True:
            temp = random.randint(30, 40)
            print(f'Temperatura no {nome} é igual a {temp}°C, em {intervalo}s irá ser medido novamente')
            sensor_data = self.database.collection.find_one({'nomeSensor': nome})
            if sensor_data and sensor_data.get('sensorAlarmado'):
                print(f"Temperatura alta, verificar o {nome}.")
                break
            alarmado = temp > 38
            update_data = {'$set': {'valorSensor': temp, 'sensorAlarmado': alarmado}}
            self.database.collection.update_one({'nomeSensor': nome}, update_data)
            time.sleep(intervalo)