from RPC_CEscucha import *
from RPC_CHabla import *
import threading

Hilo1 = threading.Thread(target=RPC_CEscucha)
Hilo2 = threading.Thread(target=RPC_CHabla)

Hilo1.start()
Hilo2.start()
