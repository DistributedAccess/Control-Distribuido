from Create_DB import *
import MySQLdb
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import Ip_Host

DB = Create_DB("root","2010020726Ev")
DB.Create_DataBase()
DB.Create_Tables()

HOST = Ip_Host.Ip_Host()

Server = xmlrpclib.ServerProxy("http://192.168.0.8:2018")

m = Server.Ingresar(HOST,'Cliente')
print(m)

db = MySQLdb.connect(user = 'root', passwd = '2010020726Ev',
                              host = '127.0.0.1',
                              db = 'CONTROL_DISTRIBUIDO')
print("Conexion establecida a la Base de Datos")

cursor = db.cursor()

Eliminar_Registros = """DELETE FROM TABLA_RUTEO """"

cursor.execute(Eliminar_Registros)

Agregar_Host = """INSERT INTO TABLA_RUTEO (Process_ID, Ip, Grupo, Coordinador, Busy)
                  VALUES(%s, %s, %s, %s, %s)"""

Id              =   None
Pid             =   None
Ip              =   None
Grup            =   None
Coor            =   None
Bus             =   None

Host_me         =   None

for i in range(len(m)):
    for j in range(len(m[i])):
        #print str(m[i][j])
        Pid     = m[i][0]
        Ip      = m[i][1]
        Grup    = m[i][2]
        Coor    = m[i][3]
        Bus     = m[i][4]


    Host_me = (Pid, Ip, Grup, Coor, Bus)
    #cursor.fetchall()
    cursor.executemany(Agregar_Host,[Host_me])


db.commit()
cursor.close()
