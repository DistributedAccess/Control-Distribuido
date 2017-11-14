import xmlrpclib
import Ip_Host

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host

Server = xmlrpclib.ServerProxy("http://localhost:2018")

Server.Registrar_Ip(HOST,'B')
print("listo mushashona")
