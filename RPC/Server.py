from RPC_SEscucha import *
from RPC_SHabla import *
import threading

Hilo1 = threading.Thread(target=RPC_SEscucha)
Hilo2 = threading.Thread(target=RPC_SHabla)

Hilo1.start()
Hilo2.start()
