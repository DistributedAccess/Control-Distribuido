import MySQLdb

class Configuracion_LBP():

    #   Variables privadas
    __User      =   'root'            #   Usuario de la Base de Datos
    __Password  =   '2010020726Ev'    #   Contrasena de la Base de Datos

    #   Variables publicas
    db          =   None          #   Objeto para la Base de Datos
    cursor      =   None          #   Objeto para la Base de Datos

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

    def Numero_Usuarios(self):
        """ Este metodo regresa el numero de usuarios """

        #   DECLARACION DE LOS OBJETOS DE LA BASE DE DATOS
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                    host = '127.0.0.1',
                                    db = 'CONTROL_DISTRIBUIDO')
        self.cursor = self.db.cursor()

        QUERY = """SELECT count(ID) FROM USUARIOS"""

        self.cursor.execute(QUERY)

        rows = self.cursor.fetchall()
        self.cursor.close()
        return rows

    def Consultar_Usuarios(self, Numero):
        """ Este metodo regresa los LBP de cada usuarios segun el numero
            de la fila"""

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                    host = '127.0.0.1',
                                    db = 'CONTROL_DISTRIBUIDO')
        self.cursor = self.db.cursor()

        QUERY = """SELECT LBP_1, LBP_2, LBP_3 FROM USUARIOS WHERE
                        ID LIMIT %s,1"""
        Host_me = Numero-1

        self.cursor.execute(QUERY,[Host_me])
        rows = self.cursor.fetchall()
        self.cursor.close()
        return rows
