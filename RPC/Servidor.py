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
Escucha = SimpleXMLRPCServer((HOST,2020)) #Configuracion del Objeto RPC
Server = Servidor_Distribuido()           #Configuracion del Objeto distribuido
#   FUNCIONES ESCUCHA
def Mensaje():
    return "Under Sky no one sees"
def Mensaje_2():
    return "The moment that you want it's comming if you give it time!"
#   INSTANCIAR FUNCIONES & CLASES ESCUCHA
Escucha.register_function(Mensaje)
Escucha.register_function(Mensaje_2)
Escucha.register_instance(Server)



#   HABLA RPC
IP_CLIENTE = None   #Direccion IP del Cliente a Comunicarse
def Hablars():
    while(True):
        Habla = xmlrpclib.ServerProxy('http://192.168.0.5:2020')
        time.sleep(3)
        print Habla.Msg()
        print Habla.Msg_2()



hilo1 = threading.Thread(target = Escucha.serve_forever)
hilo2 = threading.Thread(target = Hablars)

hilo1.start()
#hilo2.start()
