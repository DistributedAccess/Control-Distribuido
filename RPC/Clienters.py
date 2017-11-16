from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import *
import xmlrpclib
import Ip_Host

#   ESTE PROGRAMA AGREGA LA DIRECCION IP DE UN HOST
#   EXTERNO A LA BASE DE DATOS DE UN SERVIDOR TRABAJA
#   JUNTO CON Servidor.py

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host

Server = xmlrpclib.ServerProxy("http://localhost:2018")

x = Server.newip(HOST)
print("listo mushashona")
print(x)
