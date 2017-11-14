from SimpleXMLRPCServer import *
from Configuracion_Red import *
import Ip_Host


HOST   = Ip_Host.Ip_Host()    #   Obtenemos la direccion Ip de nuetro Host
PORT   = 2018

Server = SimpleXMLRPCServer(('localhost',PORT))

print ("Listening Host on: "+str('localhost')+" on Port: "+str(PORT)+"...")

Server.serve_forever()

#class Control_Distribuido:
