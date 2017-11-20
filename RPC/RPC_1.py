from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import Configuracion_Red
from Servidor_Distribuido import *
import xmlrpclib

#   Configuracion del RPC Servidor
Server = SimpleXMLRPCServer(("192.168.0.8", 2018))

#   Se inicializa la tabla de Ruteo y la Base de Datos
#   este es el unico lugar donde se mandara a llamar al
#   constructor!!!!!!!!!!
Red = Configuracion_Red('Servidor')
Red.Agregar_Propio('Servidor','Centro')

#   Se declara un objeto distribuido RPC
Servidor = Servidor_Distribuido()

#   Se declaran las rutinas que se ejecutaran de forma
#   automatica



#   Se instancian todos los metodos del objeto God
#   de la clase Servidor_Distribuido()
Server.register_instance(Servidor)
#   El servidor se pone en un ciclo infinito
Server.serve_forever()
