from SimpleXMLRPCServer import SimpleXMLRPCServer
from Cliente_Distribuido import *
from Configuracion_Red import *
import threading
import xmlrpclib
import Ip_Host
import time

#   ESCUCHA RPC
HOST = Ip_Host.Ip_Host()
Red = Configuracion_Red("Cliente")        #Configuracion de la Red y DB
Escucha = SimpleXMLRPCServer((HOST,2028)) #Configuracion del Objeto RPC
Client = Cliente_Distribuido()            #Configuracion del Objeto distribuido
#   FUNCIONES ESCUCHA
def Msg():
    return "She looks like the moon, she said it's your eyes"
def Msg_2():
    return "She said it's the light, something in the way"
#   INSTANCIAR FUNCIONES ESCUCHA
Escucha.register_function(Msg)
Escucha.register_function(Msg_2)
Escucha.register_instance(Client)



#   HABLA RPC
IP_CLIENTE = None   #Direccion IP del Cliente a Comunicarse
def Hablars():
    #   Las siguientes lineas ingresan al Servidor
    #   en la primera vez que hay conexion a este
    IP_CLIENTE = 'http://192.168.0.8:2028'          #DEFAULT
    Habla = xmlrpclib.ServerProxy(IP_CLIENTE)       #INGRESA
    Datos = Habla.Ingresar(HOST,"Cliente","Idle")   #AGREGA SU INFO
    Client.Actualizar("Cliente","Ruteo",Datos)      #ACTUALIZA SU PROPIA TR


hilo1 = threading.Thread(target = Escucha.serve_forever)
hilo2 = threading.Thread(target = Hablars)

hilo1.start()
hilo2.start()
