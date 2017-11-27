from Create_DB import *
import MySQLdb

"""     Esta clase se conecta a la Base de Datos CONTROL_DISTRIBUIDO
        en caso de no existir la clase crea la Base de Datos y sus
        respectivas tablas para el uso en Servidores o Clientes.

        Esta clase tiene relacion directa con todas las tablas de la
        Base de Datos por medio de los metodos Consultar() y Actualizar().

"""
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
            print("Constructor Base_Datos")

        except MySQLdb.DatabaseError:
            #   Se crea la Base de datos
            print("No existe la Base de Datos: CONTROL_DISTRIBUIDO")
            print("Creacion de la Base de Datos...")
            x = Create_DB(self.__User, self.__Password)
            x.Create_DataBase()
            #   Se crean las Tablas
            if (Grupo == "Servidor"):
                x.Create_Ruteo()
                x.Create_Usuarios()
                x.Create_Bitacora()
                x.Create_Laboratorio()
                x.Create_Horario()
            elif (Grupo == "Cliente"):
                x.Create_Ruteo()
                x.Create_HorarioBB()
                x.Create_UsuariosBB()
                x.Create_BitacoraBB()
            print("Constructor Base_Datos Listo!")
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
        print("Conexion establecida a la Base de Datos: CONTROL_DISTRIBUIDO")

        #   Se crea un objeto que que utilice el metodo cursor()
        #   de mysql para poder ingresar, consultar, eliminar etc. datos
        self.cursor = self.db.cursor()

        if (Opcion == "Ruteo"):
            Query = ("SELECT * FROM TABLA_RUTEO")
            self.cursor.execute(Query)

        elif (Opcion == "Usuarios"):
            Query = ("SELECT * FROM USUARIOS")
            self.cursor.execute(Query)

        elif (Opcion == "Bitacora"):
            Query = ("SELECT * FROM BITACORA")
            self.cursor.execute(Query)

        elif (Opcion == "Laboratorio"):
            Query = ("SELECT * FROM LABORATORIO")
            self.cursor.execute(Query)

        elif (Opcion == "Horario"):
            Query = ("SELECT * FROM HORARIO")
            self.cursor.execute(Query)

        elif (Opcion == "HorarioBB"):
            Query = ("SELECT * FROM HORARIOBB")
            self.cursor.execute(Query)

        elif (Opcion == "UsuariosBB"):
            Query = ("SELECT * FROM USUARIOSBB")
            self.cursor.execute(Query)

        elif (Opcion == "BitacoraBB"):
            Query = ("SELECT * FROM BITACORABB")
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

        self.cursor = self.db.cursor()


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

        elif (Opcion == "Usuarios"):
            Eliminar_Registros = """DELETE FROM USUARIOS """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO USUARIOS (ID, Nombre, Password,
                                Jerarquia, LBP_1, LBP_2, LBP_3)
                                VALUES(%s, %s, %s, %s, %s, %s, %s)"""

            Id                  = None
            Nombre              = None
            Password            = None
            Jerarquia           = None
            LBP_1               = None
            LBP_2               = None
            LBP_3               = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Id                  = Data[i][0]
                    Nombre              = Data[i][1]
                    Password            = Data[i][2]
                    Jerarquia           = Data[i][3]
                    LBP_1               = Data[i][4]
                    LBP_2               = Data[i][5]
                    LBP_3               = Data[i][6]

                Host_me = (Id, Nombre, Password, Jerarquia, LBP_1, LBP_2, LBP_3)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "Bitacora"):
            Eliminar_Registros = """DELETE FROM BITACORA """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO BITACORA (Nombre, Laboratorio,
                                Hora_Entrada)
                                VALUES(%s, %s, %s)"""

            Nombre              = None
            Laboratorio         = None
            Hora_Entrada        = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Nombre              = Data[i][0]
                    Laboratorio         = Data[i][1]
                    Hora_Entrada        = Data[i][2]

                Host_me = (Nombre, Laboratorio, Hora_Entrada)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "Laboratorio"):
            Eliminar_Registros = """DELETE FROM LABORATORIO """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO LABORATORIO (ID_Lab, Ip)
                                VALUES(%s, %s)"""

            ID_Lab              = None
            Ip                  = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    ID_Lab              = Data[i][0]
                    Ip                  = Data[i][1]

                Host_me = (ID_Lab, Ip)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "Horario"):
            Eliminar_Registros = """DELETE FROM HORARIO """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO HORARIO (Nombre, Laboratorio,
                                Grupo, Hora, Dia)
                                VALUES(%s, %s, %s, %s, %s)"""

            Nombre              = None
            Laboratorio         = None
            Grupo               = None
            Hora                = None
            Dia                 = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Nombre              = Data[i][0]
                    Laboratorio         = Data[i][1]
                    Grupo               = Data[i][2]
                    Hora                = Data[i][3]
                    Dia                 = Data[i][4]


                Host_me = (Nombre, Laboratorio, Grupo, Hora, Dia)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "HorarioBB"):
            Eliminar_Registros = """DELETE FROM HORARIOBB """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO HORARIOBB (Nombre, Grupo, Hora, Dia)
                                VALUES(%s, %s, %s, %s)"""

            Nombre              = None
            Grupo               = None
            Hora                = None
            Dia                 = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Nombre              = Data[i][0]
                    Grupo               = Data[i][1]
                    Hora                = Data[i][2]
                    Dia                 = Data[i][3]

                Host_me = (Nombre, Grupo, Hora, Dia)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "UsuariosBB"):
            Eliminar_Registros = """DELETE FROM USUARIOSBB """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO USUARIOSBB (Nombre, Password,
                                Jerarquia, LBP_1, LBP_2, LBP_3)
                                VALUES(%s, %s, %s, %s, %s, %s)"""

            Nombre              = None
            Password            = None
            Jerarquia           = None
            LBP_1               = None
            LBP_2               = None
            LBP_3               = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Nombre              = Data[i][0]
                    Password            = Data[i][1]
                    Jerarquia           = Data[i][2]
                    LBP_1               = Data[i][3]
                    LBP_2               = Data[i][4]
                    LBP_3               = Data[i][5]

                Host_me = (Nombre, Password, Jerarquia, LBP_1, LBP_2, LBP_3)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()

        elif (Opcion == "BitacoraBB"):
            Eliminar_Registros = """DELETE FROM BITACORABB """
            self.cursor.execute(Eliminar_Registros)

            Nueva_Tabla = """INSERT INTO BITACORABB (Nombre, Laboratorio)
                                VALUES(%s, %s)"""

            Nombre              = None
            Hora_Entrada        = None

            Host_me             = None

            for i in range(len(Data)):
                for j in range(len(Data[i])):
                    Nombre              = Data[i][0]
                    Hora_Entrada        = Data[i][1]

                Host_me = (Nombre, Hora_Entrada)
                self.cursor.executemany(Nueva_Tabla,[Host_me])

            self.db.commit()
            self.cursor.close()
