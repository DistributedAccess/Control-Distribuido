from Create_DB import *
import commands
import MySQLdb

    #   Esta clase se dedica exclusivamente en la...

class Base_Datos:

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

    Nom         =   None          #   Nombre del Usuario
    LBP         =   None          #   Local Binary Patern del Usuario

    Server      =   0             #   Cuenta a los Servidores conectados
    Client      =   0             #   Cuenta a los Clientes conectados

    def __init__(self, Grupo):
        #   Constructor de la clase, que  establece la conexion a
        #   la Base de Datos. En caso de no existir la Base de Datos
        #   se ejecutara el programa Create_DB.py para crear la Base
        #   de Datos.

        try:
            self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                          host = '127.0.0.1',
                                          db = 'CONTROL_DISTRIBUIDO')
            print("Conexion establecida a la Base de Datos")
            print("Constructor BD")

        except MySQLdb.DatabaseError:
            #   Se crea la Base de datos
            print("No existe la Base de Datos")
            print("Creacion de la Base de Datos...")
            x = Create_DB(self.__User, self.__Password)
            x.Create_DataBase()
            #   Se crean las Tablas
            if (Grupo == "Servidor"):
                x.Create_Ruteo()
                x.Create_ReplicaTotal()
            elif (Grupo == "Cliente"):
                x.Create_Ruteo()
                x.Create_ReplicaParcial()
            print("Constructor BD")
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

    def Actualizar(self, Grupo, Opcion, Data):
        #   Actualizar recibe las tablas de las bases de
        #   datos a Actualizar dependiendo del grupo y
        #   que tipo de tabla a actualizar
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                      host = '127.0.0.1',
                                      db = 'CONTROL_DISTRIBUIDO')
        print("Conexion establecida a la Base de Datos")

        self.cursor = self.db.cursor()

        if (Grupo == "Servidor"):
            if (Opcion == "Ruteo"):
                Eliminar_Registros = """DELETE FROM TABLA_RUTEO """
                self.cursor.execute(Eliminar_Registros)

                Nueva_Tabla = """INSERT INTO TABLA_RUTEO (Process_ID,
                                    Laboratorio, Ip, Grupo, Coordinador)
                                    VALUES(%s, %s, %s, %s, %s)"""

                self.Pro_Id         = None
                self.Lab            = None
                self.Ip             = None
                self.Grupo          = None
                self.Coordinador    = None

                Host_me             = None

                for i in range(len(Data)):
                    for j in range(len(Data[i])):
                        self.Pro_Id         = Data[i][0]
                        self.Lab            = Data[i][1]
                        self.Ip             = Data[i][2]
                        self.Grupo          = Data[i][3]
                        self.Coordinador    = Data[i][4]

                    Host_me = (self.Pro_Id, self.Lab, self.Ip, self.Grupo, self.Coordinador)
                    self.cursor.executemany(Nueva_Tabla,[Host_me])

                self.db.commit()
                self.cursor.close()

            elif (Opcion == "Total"):
                Eliminar_Registros = """DELETE FROM USUARIOS """
                self.cursor.execute(Eliminar_Registros)

                Nueva_Tabla = """INSERT INTO USUARIOS (Nombre, LBP, Laboratorio)
                                    VALUES(%s, %s, %s)"""

                self.Nom            = None
                self.LBP            = None
                self.Lab            = None

                Host_me             = None

                for i in range(len(Data)):
                    for j in range(len(Data[i]))
                        self.Nom            = Data[i][0]
                        self.LBP            = Data[i][1]
                        self.Lab            = Data[i][2]

                    Host_me = (self.Nom, self.LBP, self.Lab)
                    self.cursor.executemany(Nueva_Tabla,[Host_me])

                self.db.commit()
                self.cursor.close()

        elif (Grupo == "Cliente"):
            if (Opcion == "Ruteo"):
                Eliminar_Registros = """DELETE FROM TABLA_RUTEO """
                self.cursor.execute(Eliminar_Registros)

                Nueva_Tabla = """INSERT INTO TABLA_RUTEO (Process_ID,
                                    Laboratorio, Ip, Grupo, Coordinador)
                                    VALUES(%s, %s, %s, %s, %s)"""

                self.Pro_Id         = None
                self.Lab            = None
                self.Ip             = None
                self.Grupo          = None
                self.Coordinador    = None

                Host_me             = None

                for i in range(len(Data)):
                    for j in range(len(Data[i])):
                        self.Pro_Id         = Data[i][0]
                        self.Lab            = Data[i][1]
                        self.Ip             = Data[i][2]
                        self.Grupo          = Data[i][3]
                        self.Coordinador    = Data[i][4]

                    Host_me = (self.Pro_Id, self.Lab, self.Ip, self.Grupo, self.Coordinador)
                    self.cursor.executemany(Nueva_Tabla,[Host_me])

                self.db.commit()
                self.cursor.close()

            elif (Opcion == "Replica"):
                Eliminar_Registros = """DELETE FROM USUARIOS_REPLICA """
                self.cursor.execute(Eliminar_Registros)

                Nueva_Tabla = """INSERT INTO USUARIOS_REPLICA (Nombre, LBP)
                                    VALUES(%s, %s)"""

                self.Nom            = None
                self.LBP            = None

                Host_me             = None

                for i in range(len(Data)):
                    for j in range(len(Data[i]))
                        self.Nom            = Data[i][0]
                        self.LBP            = Data[i][1]

                    Host_me = (self.Nom, self.LBP)
                    self.cursor.executemany(Nueva_Tabla,[Host_me])

                self.db.commit()
                self.cursor.close()
