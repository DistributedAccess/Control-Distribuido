from SimpleXMLRPCServer import SimpleXMLRPCServer
from Cliente_Distribuido import *
from Configuracion_Red import *
from Ip_Host import *

HOST = Ip_Host()

#   OBJETO DE RED
Red = Configuracion_Red("Cliente")

#   OBJETO DE ESCUCHA
Escucha = SimpleXMLRPCServer((HOST,2012))
Escucha.register_instance(Cliente_Distribuido())

Escucha.serve_forever()
