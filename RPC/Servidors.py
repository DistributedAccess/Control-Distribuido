from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Configuracion_Red import *
import Ip_Host

#   ESTE PROGRAMA AGREGA LA DIRECCION IP DE UN HOST
#   EXTERNO A LA BASE DE DATOS TRABAJA JUNTO CON
#   Cliente.py

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host
PORT = 2018                                 #PORT = Puerto de comunicacion
Server = SimpleXMLRPCServer(('localhost', PORT))   #Se crea el servidor RPC
Server.register_introspection_functions()

Red = Configuracion_Red()  #Se accede a la configuracion de Red

def Registrar_Ip(Host_Externo):
    #   NO MODIFICAR YA ESTA!!!
    #   Esta funcion se encarga de registrar la Direccion
    #   Ip de los host que se conectan al RPC es necesario
    #   que siempre se ejecute al principio

    Red.Agregar_Host(Host_Externo,'C')
    print("Se ha agregado el Host: ", Host_Externo)
    return "OK"

print("Listening...")
Server.register_function(Registrar_Ip,'newip')



Server.serve_forever()
