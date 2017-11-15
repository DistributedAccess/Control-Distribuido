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
    Pro_Id      =   None          #   Numero del process Id
    Ip          =   None          #   Direccion Ip
    Grupo       =   None          #   Tipo de Host Cliente o Servidor
    Coordinador =   None          #   Bandera del Coordinador
    Busy       =   None          #   Bandera de Estado Ocupado/Desocupado


    def __init__(self):
        #   Constructor de la clase, que  establece la conexion a
        #   la Base de Datos, en caso de no conectarse se llamara
        #   automaticamente al metodo Conec_DB(self, user, password)
        #   que le pedira al usuario ingresar manualmente el Usuario
        #   y Contrasena para tener acceso a la Base de Datos. En
        #   caso de no existir la Base de Datos se ejecutara el programa
        #   Create_DB.py para crear la Base de Datos.

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                          host = '127.0.0.1',
                                          database = 'CONTROL_DISTRIBUIDO')
            print("Conexion establecida a la Base de Datos")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                #   Se corrige al usuario y la contrasena
                print("Hay un error de escritura en el Usuario y la Contrasena")
                Usu = raw_input("Introduce el usuario: ")
                Pas = raw_input("Introduce la contrasena: ")
                self.Conec_DB(Usu, Pas)

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                #   Se crea la Base de datos
                print("No existe la Base de Datos")
                print("Creacion de la Base de Datos...")

                x = Create_DB(self.__User, self.__Password)
                x.Create_DataBase()
                x.Create_Tables()

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
                                      database = 'CONTROL_DISTRIBUIDO')

    def Disco_DB(self):
        #   Esta funcion desconectara el objeto de la
        #   Base de datos.
        self.cnx.close()
        self.cursor.close()
        print("Desconexion de la Base de Datos")

    def Agregar_Propio(self):
        #   Esta funcion agrega a la Base de Datos la direccion
        #   Ip del Host, asegurandose que la direccion sea unica
        #   en la tabla de ruteo.

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        self.Pro_Id         = 0
        self.Ip             = self.Ip_Host()
        self.Grupo          = 'Servidor'
        self.Coordinador    = 0
        self.Busy           = 0

        Host_me = (self.Pro_Id, self.Ip, self.Grupo, self.Coordinador, self.Busy)

        #   Eliminar Host para asegurar que este sea el
        #   unico en la Tabla de Ruteo
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % self.Ip)
        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        #   Se agrega el Host a la Tabla de Ruteo
        Agregar_Host = ("INSERT INTO TABLA_RUTEO (Process_ID, Ip, Grupo, Coordinador, Busy)"
                        "VALUES(%s, %s, %s, %s, %s)")
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
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Ip = self.Ip_Host()
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)

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
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        self.Pro_Id         = 0
        self.Ip             = Ip
        self.Grupo          = Grupo
        self.Coordinador    = 0
        self.Busy           = 0

        Host_me = (self.Pro_Id, self.Ip, self.Grupo, self.Coordinador, self.Busy)

        #   Eliminar Host para asegurar que este sea el
        #   unico en la Tabla de Ruteo
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)
        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        #   Se agrega el Host a la Tabla de Ruteo
        Agregar_Host = ("INSERT INTO TABLA_RUTEO (Process_ID, Ip, Grupo, Coordinador, Busy)"
                        "VALUES(%s, %s, %s, %s, %s)")
        self.cursor.execute(Agregar_Host, Host_me)
        print("Se ha agregado una direccion")

        self.cnx.commit()
        self.cursor.close()

        #   La funcion ID_Proceso debera ejecutarse despues
        #   de self.cnx.commit() y self.cursor.close() para
        #   evitar inconsistencias
        self.ID_Proceso(Ip, Grupo)

    def Eliminar_Host(self, Ip):
        #   Esta funcion elimina de la Base de Datos direcciones Ip,
        #   externas al host

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)

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
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        Query = ("SELECT * FROM TABLA_RUTEO")

        self.cursor.execute(Query)

        for(ID, Process_ID, IP, Grupo, Coordinador, Busy) in self.cursor:
            print(ID, Process_ID, IP, Grupo, Coordinador, Busy)

        self.cursor.close()

    def ID_Proceso(self, Ip, Grupo):
        #   Esta funcion se encarga de asignar el Process_ID
        #   a los Hosts de la red.

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                      host = '127.0.0.1',
                                      database = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.cnx.cursor()

        if(Grupo == "Servidor"):

            Query =  ("""SELECT Process_ID FROM TABLA_RUTEO
                      WHERE Grupo='Servidor' AND
                      Process_ID=(SELECT MAX(Process_ID)
                      FROM TABLA_RUTEO)""")
            self.cursor.execute(Query)

            #   Pequena rutina para obener el Process_ID
            #   anterior :)
            for(Process_ID) in self.cursor:
                ANT = Process_ID
            ANTERIOR = str(ANT)
            Coma = ANTERIOR.find(",")
            ANTERIOR = ANTERIOR[1:Coma]
            A = int(ANTERIOR)
            A = A + 1     #   Se incrementa Anterior
            print(A)

            print("Metiste un servidor")
            #print(Ip)

        elif(Grupo == "Cliente"):

            Query = ("""SELECT Process_ID FROM TABLA_RUTEO
                     WHERE Grupo='Cliente' AND
                     Process_ID=(SELECT MAX(Process_ID)
                     FROM TABLA_RUTEO)""")
            self.cursor.execute(Query)

            #   Pequena rutina para obener el Process_ID
            #   anterior :)
            for(Process_ID) in self.cursor:
                ANT = Process_ID
            ANTERIOR = str(ANT)
            Coma = ANTERIOR.find(",")
            ANTERIOR = ANTERIOR[1:Coma]

            #self.cursor.execute(Query)
            print("Metiste un Cliente")
            #print(Ip)

        self.cursor.close()

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
