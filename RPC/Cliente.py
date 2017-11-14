from SimpleXMLRPCServer import SimpleXMLRPCServer
from Configuracion_Red import *
import xmlrpclib
import Ip_Host

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host

Server = xmlrpclib.ServerProxy("http://localhost:2018")

x = Server.newip(HOST)
print("listo mushashona")
print(x)
