from SimpleXMLRPCServer import SimpleXMLRPCServer
from Servidor_Distribuido import *
from Configuracion_Red import *
from Ip_Host import *

HOST = Ip_Host()

#   OBJETO DE RED
Red = Configuracion_Red("Servidor")
Red.Agregar_Propio("Servidor", "LOCAL", 1)

#   OBJETO DE ESCUCHA
Escucha = SimpleXMLRPCServer((HOST,2019))
Escucha.register_instance(Servidor_Distribuido())

Escucha.serve_forever()
