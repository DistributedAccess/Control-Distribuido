from Create_DB import *
import commands
import MySQLdb

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

class Configuracion_Red:

    #   Variables privadas
    __User      =   'root'            #   Usuario de la Base de Datos
    __Password  =   '2010020726Ev'    #   Contrasena de la Base de Datos

    #   Variables publicas
    db          =   None          #   Objeto para la Base de Datos
    cursor      =   None          #   Objeto para la Base de Datos
    Pro_Id      =   None          #   Numero del process Id
    Lab         =   None          #   Identificador del Laboratorio
    Ip          =   None          #   Direccion Ip
    Grupo       =   None          #   Tipo de Host Cliente o Servidor
    Coordinador =   None          #   Bandera del Coordinador
    Server      =   0             #   Cuenta a los Servidores conectados
    Client      =   0             #   Cuenta a los Clientes conectados


    def __init__(self, Grupo):
        #   Constructor de la clase, que  establece la conexion a
        #   la Base de Datos, en caso de no conectarse se llamara
        #   automaticamente al metodo Conec_DB(self, user, password)
        #   que le pedira al usuario ingresar manualmente el Usuario
        #   y Contrasena para tener acceso a la Base de Datos. En
        #   caso de no existir la Base de Datos se ejecutara el programa
        #   Create_DB.py para crear la Base de Datos.

        try:
            self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                          host = '127.0.0.1',
                                          db = 'CONTROL_DISTRIBUIDO')
            print("Conexion establecida a la Base de Datos")

        except MySQLdb.DatabaseError:
            #   Se crea la Base de datos
            print("No existe la Base de Datos")
            print("Creacion de la Base de Datos...")
            x = Create_DB(self.__User, self.__Password)
            x.Create_DataBase()

            if (Grupo == "Servidor"):
                x.Create_Ruteo()
                x.Create_ReplicaTotal()
            elif (Grupo == "Cliente"):
                x.Create_Ruteo()
                x.Create_ReplicaParcial()

        else:
            self.db.close()

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

        self.db = MySQLdb.connect(user = user, passwd = password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        return "OK"

    def Disco_DB(self):
        #   Esta funcion desconectara el objeto de la
        #   Base de datos.
        self.db.close()
        self.cursor.close()
        print("Desconexion de la Base de Datos")
        return "OK"

    def Agregar_Propio(self, Grupo, Laboratorio):
        #   Esta funcion agrega a la Base de Datos la direccion
        #   Ip del Host, asegurandose que la direccion sea unica
        #   en la tabla de ruteo.

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        self.Pro_Id         = 0
        self.Lab            = Laboratorio
        self.Ip             = self.Ip_Host()
        self.Grupo          = Grupo
        self.Coordinador    = 0

        Host_me = (self.Pro_Id, self.Lab, self.Ip, self.Grupo, self.Coordinador)

        #   Eliminar Host para asegurar que este sea el
        #   unico en la Tabla de Ruteo
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % self.Ip)
        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        #   Se agrega el Host a la Tabla de Ruteo
        Agregar_Host = """INSERT INTO TABLA_RUTEO (Process_ID, Laboratorio, Ip, Grupo, Coordinador)
                          VALUES(%s, %s, %s, %s, %s)"""

        self.cursor.fetchall()
        self.cursor.executemany(Agregar_Host,[Host_me])

        print("Se ha agregado una direccion")

        self.db.commit()
        self.cursor.close()

        self.ID_Proceso(self.Ip,self.Grupo)

    def Eliminar_Propio(self):
        #   Esta funcion elimina de la Base de Datos la direccion
        #   Ip del Host

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        Ip = self.Ip_Host()
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        self.db.commit()
        self.cursor.close()

    def Agregar_Host(self, Ip, Grupo, Laboratorio):
        #   Esta funcion agrega a la Base de Datos direcciones Ip,
        #   externas al host, asegurandose que la direccion sea unica
        #   en la tabla de ruteo

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        self.Pro_Id         = 0
        self.Lab            = Laboratorio
        self.Ip             = Ip
        self.Grupo          = Grupo
        self.Coordinador    = 0

        Host_me = (self.Pro_Id, self.Lab, self.Ip, self.Grupo, self.Coordinador)

        #   Eliminar Host para asegurar que este sea el
        #   unico en la Tabla de Ruteo
        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)
        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        #   Se agrega el Host a la Tabla de Ruteo
        Agregar_Host = """INSERT INTO TABLA_RUTEO (Process_ID, Laboratorio, Ip, Grupo, Coordinador)
                          VALUES(%s, %s, %s, %s, %s)"""

        self.cursor.fetchall()
        self.cursor.executemany(Agregar_Host,[Host_me])
        print("Se ha agregado una direccion")

        self.db.commit()
        self.cursor.close()

        self.ID_Proceso(Ip,Grupo)
        return "OK"

    def Eliminar_Host(self, Ip):
        #   Esta funcion elimina de la Base de Datos direcciones Ip,
        #   externas al host

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        Eliminar_Host =  ("DELETE FROM TABLA_RUTEO WHERE IP = '%s'" % Ip)

        self.cursor.execute(Eliminar_Host)
        print("Se ha eliminado una direccion")

        self.db.commit()
        self.cursor.close()
        return "OK"

    def Consultar(self, Opcion):
        #   Esta funcion consulta las tablas
        #   de la Base de Datos

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        if (Opcion == "Ruteo"):
            Query = ("SELECT * FROM TABLA_RUTEO")
            self.cursor.execute(Query)

        elif (Opcion == "Total"):
            Query = ("SELECT * FROM USUARIOS")
            self.cursor.execute(Query)

        elif (Opcion == "Replica"):
            Query = ("SELECT * FROM USUARIOS_REPLICA")
            self.cursor.execute(Query)

        rows = self.cursor.fetchall()
        self.cursor.close()
        return rows

    def ID_Proceso(self, Ip, Grupo):
        #   Esta funcion se encarga de asignar el Process_ID
        #   a los Hosts de la red. Cabe aclarar que esta funcion
        #   es llamada cada que se guarda un Host en la red
        #   por las funciones: Agregar_Propio(self) y
        #   Agregar_Host(self, Ip, Grupo)
        #
        #   La forma de incremetar el Process_ID es de lo mas
        #   sencillo se tienen dos variables publicas Server y
        #   Cliente que incrementan cada que se registra un host
        #   el problema viene cuando el host se desconecta y vuelve
        #   a comenzar las variables volveran a contar desde cero.
        #   Puede suponer o no un problema, dependiendo el caso
        #   para ello se deben tener protocolos de deteccion de
        #   errores.
        #
        #   ESTA FUNCION DEBERA SER USADA POR EL COORDINADOR
        #   DEL GRUPO.

        #   Es necesario volver a conectarse con la base de datos
        #   para poder ingresar datos en las tablas
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        A = 0

        if(Grupo == "Servidor"):
            A = self.Server
            A = A + 1
            self.Server = A

        elif(Grupo == "Cliente"):
            A = self.Client
            A = A + 1
            self.Client = A

        Update = ("""UPDATE TABLA_RUTEO SET
                     Process_ID = '%s'
                     WHERE IP = '%s'""" %(A,Ip))

        self.cursor.execute(Update)

        self.db.commit()
        self.cursor.close()
        self.db.close()

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
