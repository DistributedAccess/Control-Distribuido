from SimpleXMLRPCServer import SimpleXMLRPCServer
from Cliente_Distribuido import *
import xmlrpclib

#   Configuracion del RPC Cliente
Server = xmlrpclib.ServerProxy("http://192.168.0.8:2018")

#   Se declara un objeto distribuido RPC
Cliente = Cliente_Distribuido()
