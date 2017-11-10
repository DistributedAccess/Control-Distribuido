import commands
from mysql.connector import (connection)

def Ip_Host():
    #   Esta funcion regresa la direccion ip del Host
    #   a traves de la libreria commands se ejecuta
    #   el programa hostname de Linux y lo que regresa
    #   se guarda en una variable para posteriormente
    #   separar la direccion que nos interesa

    Ip = commands.getoutput("hostname -I")
    Espacio = Ip.find(" ")
    Ip = Ip[0:Espacio]
    return Ip



cnx = connection.MySQLConnection(user = 'root', password = '2010020726Ev',
                                 host = '127.0.0.1',
                                 database = 'TablaRuteo')
cursor = cnx.cursor()

Agregar_Host = ("INSERT INTO Ruteo (Grupo, IP)"
                "VALUES(%s, %s)")

A = 'Grupo A'
Ip = Ip_Host()

Host_me = (A, Ip)

cursor.execute(Agregar_Host, Host_me)



cnx.commit()
cursor.close()
cnx.close()

print("Listo se ha agredado el host")
