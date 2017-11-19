from mysql.connector import errorcode
import MySQLdb
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib


Server = xmlrpclib.ServerProxy("http://localhost:2018")


m = Server.Ingresar('11.5.20.18','Servidor')
print(m)

db = MySQLdb.connect(user = 'root', passwd = '2010020726Ev',
                              host = '127.0.0.1',
                              db = 'CONTROL_DISTRIBUIDO')
print("Conexion establecida a la Base de Datos")

cursor = db.cursor()

#Host_me = (self.Pro_Id, self.Ip, self.Grupo, self.Coordinador, self.Busy)
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
        Id      = m[i][0]
        Pid     = m[i][1]
        Ip      = m[i][2]
        Grup    = m[i][3]
        Coor    = m[i][4]
        Bus     = m[i][5]

        
    Host_me = (Id, Pid, Ip, Grup, Coor, Bus)
    cursor.fetchall()
    cursor.executemany(Agregar_Host,[Host_me])


cnx.commit()
cursor.close()
