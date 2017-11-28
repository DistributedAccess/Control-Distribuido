from Cliente_Distribuido import *
import xmlrpclib
from Ip_Host import *

#   VARIABLES
HOST = Ip_Host()
SERVIDOR = 'http://192.168.0.8:2012'

#   OBJETOS
Habla = xmlrpclib.ServerProxy(SERVIDOR)
Client = Cliente_Distribuido()


if __name__ == "__main__":

    Datos = Habla.Ingresar(HOST,"Cliente","Idle")   #AGREGA SU INFO
    Client.Actualizare("Cliente","Ruteo",Datos,"2012")      #ACTUALIZA SU PROPIA TR
