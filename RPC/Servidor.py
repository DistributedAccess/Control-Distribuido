from SimpleXMLRPCServer import SimpleXMLRPCServer
from Servidor_Distribuido import *
from Configuracion_Red import *
import threading
import xmlrpclib
import Ip_Host
import time

#   ESCUCHA RPC
HOST = Ip_Host.Ip_Host()
Red = Configuracion_Red("Servidor")       #Configuracion de la Red y DB
Red.Agregar_Propio("Servidor","LOCAL",1)    #Agregar host propio a la DB
Escucha = SimpleXMLRPCServer((HOST,2020)) #Configuracion del Objeto RPC
Server = Servidor_Distribuido()           #Configuracion del Objeto distribuido


#   FUNCIONES ESCUCHA

Escucha.register_instance(Server)





hilo1 = threading.Thread(target = Escucha.serve_forever)

hilo1.start()
#hilo2.start()
