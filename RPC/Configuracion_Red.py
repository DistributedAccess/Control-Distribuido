from mysql.connector import errorcode
import mysql.connector
from Create_DB import *
import commands

class Configuracion_Red:
    #   Esta clase se dedica exclusivamente en la configuracion
    #   de los Hosts en la red de Control_Distribuido. Los Hosts
    #   ya sean Cliete o Servidor pueden hacer uso de los metodos
    #   de esta clase, las reglas de su respectivo uso estan
    #   determinadas por el tipo de objeto al que correspondan.
    #
    #   La configuracion que realiza esta clase esta relacionada
    #   con la tabla de ruteo de los Hosts asi como el acceso a
    #   la Base de Datos.
    #
    #   Cabe aclarar que la clase debera acceder a una Base de
    #   Datos con las siguientes caracteristicas:
    #
    #   Base de Datos:  CONTROL_DISTRIBUIDO
    #   Tabla:          TABLA_RUTEO
    #
    #   Si no se cuenta con tal Base de Datos se debera ejecutar
    #   el programa Create_DB.py una vez, para hacer dichas
    #   configuraciones, la creacion de la base de datos puede ser
    #   manual o puede hacerse desde el constructor __init__.

    #   Variables privadas
    __User        =   'root'            #   Usuario de la Base de Datos
    __Password    =   '2010020726Ev'    #   Contrasena de la Base de Datos

    #   Variables publicas
    cnx         =   None          #   Objeto para la Base de Datos
    cursor      =   None          #   Objeto para la Base de Datos
    Ip          =   None          #   Direccion Ip
    Id          =   None          #   Numero de Id
    Grupo       =   None          #   Grupo del Host
    Tipo_Host   =   None          #   Tipo de Host, Cliete o Servidor
    Coordinador =   None          #   Bandera del Coordinador
    Busy        =   None          #   Bandera de Estado Ocupado/Desocupado


    def __init__(self):
        #   Constructor de la clase, que  establece la conexion a
        #   la Base de Datos, en caso de no conectarse se llamara
        #   automaticamente al metodo Conec_DB(self, user, password)
        #   que le pedira al usuario ingresar manualmente el Usuario
        #   y Contrasena para tener acceso a la Base de Datos. En
        #   caso de no existir la Base de Datos se ejecutara el programa
        #   Create_DB.py para crear la Base de Datos.
        #

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
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
            self.cnx.close()

    def Conec_DB(self, user, password):
        #   Esta funcion establece la conexion entre el objeto a
        #   la Base de Datos de modo que el usuario debera ingresar
        #   el Usuario y la Contrasena para poder tener acceso a
        #   la Base de Datos.

        self.U = user
        self.P = password

        #   Se actualizan las variables privadas para
        #   el inicio de sesion de la Base de Datos
        self.__User = user
        self.__Password = password

        self.cnx = mysql.connector.connect(user = user, password = password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')


    def Disco_DB(self):
        #   Esta funcion desconectara el objeto de la
        #   Base de datos.
        self.cnx.close()
        self.cursor.close()
        print("Desconexion de la Base de Datos")

    def Agregar_Propio(self):
        #   Esta funcion agrega a la Base de Datos la direccion
        #   Ip del Host, asegurandose que la direccion sea unica
        #   en la tabla de ruteo

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        A = 'Grupo A'
        Ip = self.Ip_Host()
        Host_me = (A, Ip)

        Agregar_Host = ("INSERT INTO Ruteo (Grupo, IP)"
                        "VALUES(%s, %s)")

        Eliminar_Host =  ("DELETE FROM Ruteo WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        self.cursor.execute(Agregar_Host, Host_me)
        print("Se ha agregado una direccion")

        self.cnx.commit()
        self.cursor.close()

    def Eliminar_Propio(self):
        #   Esta funcion elimina de la Base de Datos la direccion
        #   Ip del Host

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Ip = self.Ip_Host()
        Eliminar_Host =  ("DELETE FROM Ruteo WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        self.cnx.commit()
        self.cursor.close()

    def Agregar_Host(self, Ip, Grupo):
        #   Esta funcion agrega a la Base de Datos direcciones Ip,
        #   externas al host, asegurandose que la direccion sea unica
        #   en la tabla de ruteo

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Host_me = (Grupo, Ip)

        Agregar_Host = ("INSERT INTO Ruteo (Grupo, IP)"
                        "VALUES(%s, %s)")

        Eliminar_Host =  ("DELETE FROM Ruteo WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        self.cursor.execute(Agregar_Host, Host_me)
        print("Se ha agregado una direccion")

        self.cnx.commit()
        self.cursor.close()

    def Eliminar_Host(self, Ip):
        #   Esta funcion elimina de la Base de Datos direcciones Ip,
        #   externas al host

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Eliminar_Host =  ("DELETE FROM Ruteo WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")



        self.cnx.commit()
        self.cursor.close()

    def Consultar(self):
        #   Esta funcion consulta a la Base de Datos la tabla
        #   de ruteo

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'TablaRuteo')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Query = ("SELECT * FROM Ruteo")

        self.cursor.execute(Query)

        for(ID, Grupo, IP) in self.cursor:
            print(ID, Grupo, IP)

        self.cursor.close()
        self.cnx.close()

    def Ip_Host(self):
        #   Esta funcion regresa la direccion ip del Host
        #   a traves de la libreria commands se ejecuta
        #   el programa hostname de Linux y lo que regresa
        #   se guarda en una variable para posteriormente
        #   separar la direccion que nos interesa

        Ip = commands.getoutput("hostname -I")
        Espacio = Ip.find(" ")
        Ip = Ip[0:Espacio]
        return Ip
