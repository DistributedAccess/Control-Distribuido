import MySQLdb

class Configuracion_LBP():

    #   Variables privadas
    __User      =   'root'            #   Usuario de la Base de Datos
    __Password  =   '2010020726Ev'    #   Contrasena de la Base de Datos

    #   Variables publicas
    db          =   None          #   Objeto para la Base de Datos
    cursor      =   None          #   Objeto para la Base de Datos

    def __init__(self):

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                    host = '127.0.0.1',
                                    db = 'CONTROL_DISTRIBUIDO')
        print("Conexion a la Base de Datos: CONTROL_DISTRIBUIDO")
        print("Constructor de Configuracion_Red Listo!")


    def Asignar_LBP(self, Id_Usuario, Data1, Data2, Data3):
        """ Este metdo ingresa el LBP_1, LBP_2 y LBP_3 de los usuarios
            por medio del ID de la tabla USUARIO.
        """

        #   DECLARACION DE LOS OBJETOS DE LA BASE DE DATOS
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                    host = '127.0.0.1',
                                    db = 'CONTROL_DISTRIBUIDO')
        self.cursor = self.db.cursor()

        #   DECLARACION DEL QUERY
        UPDATE = """UPDATE USUARIOS SET LBP_1=%s, LBP_2=%s, LBP_3=%s
                            WHERE ID=%s"""
        Host_me = (Data1, Data2, Data3, Id_Usuario)

        self.cursor.executemany(UPDATE,[Host_me])

        self.db.commit()
        self.cursor.close()

    def Numero_Usuarios():
        """ Este metodo regresa el numero de usuarios """

        #   DECLARACION DE LOS OBJETOS DE LA BASE DE DATOS
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                    host = '127.0.0.1',
                                    db = 'CONTROL_DISTRIBUIDO')
        self.cursor = self.db.cursor()

        QUERY = """SELECT count(ID) FROM USUARIOS"""

        self.cursor.execute(QUERY)
        self.cursor.close()

    def Consultar_Usuarios():
        pass
