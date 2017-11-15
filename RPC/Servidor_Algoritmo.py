from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Configuracion_Red import *
import Ip_Host

#   ESTE PROGRAMA AGREGA LA DIRECCION IP DE UN HOST
#   EXTERNO A LA BASE DE DATOS Y AGREGA EL PROCESS_ID
#   TRABAJA JUNTO CON Cliente.py

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host
PORT = 2018                                 #PORT = Puerto de comunicacion
Server = SimpleXMLRPCServer(('localhost', PORT))   #Se crea el servidor RPC
Server.register_introspection_functions()

Red = Configuracion_Red()  #Se accede a la configuracion de Red

def Registrar_Ip(Host_Externo, Grupo_Externo):
    #   NO MODIFICAR YA ESTA!!!
    #   Esta funcion se encarga de registrar la Direccion
    #   Ip de los host que se conectan al RPC es necesario
    #   que siempre se ejecute al principio

    Red.Agregar_Host(Host_Externo,Grupo_Externo)
    print("Se ha agregado el Host: ", Host_Externo)
    print("Se ha agregado al Grupo: ", Grupo_Externo)
    return "OK"

print("Listening...")
Server.register_function(Registrar_Ip,'newip')



Server.serve_forever()
