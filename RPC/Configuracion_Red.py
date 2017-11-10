import mysql.connector
from mysql.connector import errorcode
import commands                                 #   Para el uso de comandos Linux

class Configuracion_Red:

    #   Variables privadas
    _User        =   'root'
    _Password    =   '2010020726Ev'

    def __init__(self, user, password):
        #   Esta funcion puede ser considerada como un
        #   constructor ya que cuando se instancia una clase
        #   esta se inicializa. Este constructor se conecta a
        #   la base de datos.
        self.U = user
        self.P = password

        #   Se actualizan las variables privadas para
        #   el inicio de sesion de la Base de Datos
        self._User = user
        self._Password = password

        #   Se conecta a la base de datos, si hay algun
        #   error en la conexion este te avisara.
        try:
            cnx = mysql.connector.connect(user = user, password = password,
                                          host = '127.0.0.1',
                                          database = 'TablaRuteo')
            print("Conexion establecida a la Base de Datos")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Hay un error de escritura en el Usuario y la Contrasena")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe la Base de Datos")
            else:
                print(err)
        else:
            cnx.close()

    def Conec_DB():
        #   Esta funcion conectara el objeto a la Base
        #   de datos, por primera vez o cada que halla
        #   una desconexion hacia ella.

        try:
            cnx = mysql.connector.connect(user = _User, password = _Password,
                                          host = '127.0.0.1',
                                          database = 'TablaRuteo')
            print("Conexion establecida a la Base de Datos")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Hay un error de escritura en el Usuario y la Contrasena")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe la Base de Datos")
            else:
                print(err)
        else:
            cnx.close()


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
