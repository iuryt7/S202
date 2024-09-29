import threading

from Thread import Sensores
from database import Database
from database import Database

db = Database(database="bancoiot", collection="sensores")
sensores = Sensores(db)
threads = []
for i in range(1, 4):
    t = threading.Thread(target=sensores.sensor, args=(f"Sensor{i}", 5))
    t.start()
    threads.append(t)