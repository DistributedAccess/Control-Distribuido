from SimpleXMLRPCServer import SimpleXMLRPCServer
import Ip_Host

HOST = Ip_Host.Ip_Host()                    #HOST = Direccion Ip del Host
PORT = 2018                                 #PORT = Puerto de comunicacion

Server = SimpleXMLRPCServer((HOST, PORT))   #Se crea el servidor RPC
