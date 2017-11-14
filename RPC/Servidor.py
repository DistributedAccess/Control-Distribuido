from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import *
import Ip_Host

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host
PORT = 2018                                 #PORT = Puerto de comunicacion
Server = SimpleXMLRPCServer(('localhost', PORT))   #Se crea el servidor RPC
Server.register_introspection_functions()

Red = Configuracion_Red('root','2010020726Ev')  #Se accede a la configuracion de Red

def Registrar_Ip(Host_Externo,Group):
    Red.Agregar_Host(Host_Externo,Group)
    print("Se ha agregado el Host: ", Host_Externo)

Server.register_function(Registrar_Ip)

Server.serve_forever()
