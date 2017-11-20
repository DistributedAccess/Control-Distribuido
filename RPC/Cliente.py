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
Escucha = SimpleXMLRPCServer((HOST,2020)) #Configuracion del Objeto RPC
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
    IP_CLIENTE = 'http://192.168.0.8:2020'      #DEFAULT
    Habla = xmlrpclib.ServerProxy(IP_CLIENTE)
    Datos = Habla.Ingresar(HOST,"Cliente","Idle")
    Client.Actualizar("Cliente","Ruteo",Datos)
    '''while(True):
        Habla = xmlrpclib.ServerProxy('http://192.168.0.8:2020')
        time.sleep(3)
        print Habla.Mensaje()
        print Habla.Mensaje_2()'''



hilo1 = threading.Thread(target = Escucha.serve_forever)
hilo2 = threading.Thread(target = Hablars)

hilo1.start()
hilo2.start()
