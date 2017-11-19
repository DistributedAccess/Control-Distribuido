from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import Configuracion_Red
from Servidor_Distribuido import *

#   Configuracion del RPC
Server = SimpleXMLRPCServer(("192.168.0.8", 2018))

#   Se inicializa la tabla de Ruteo y la Base de Datos
#   este es el unico lugar donde se mandara a llamar al
#   constructor!!!!!!!!!!
Red = Configuracion_Red()
Red.Agregar_Propio('Servidor')

#   Se declara un objeto distribuido
God = Servidor_Distribuido()

#   Se instancian todos los metodos del objeto God
#   de la clase Servidor_Distribuido()

Server.register_instance(God)

Server.serve_forever()
