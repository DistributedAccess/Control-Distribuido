from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import *
import xmlrpclib
import Ip_Host

#HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host

Server = xmlrpclib.ServerProxy("http://localhost:2018")

HOST = raw_input("Direccion IP: ")
GRUPO = raw_input("Grupo: ")
x = Server.newip(HOST,GRUPO)
print("listo mushashona")
print(x)
