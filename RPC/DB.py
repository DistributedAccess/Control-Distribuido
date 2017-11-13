from mysql.connector import errorcode
import mysql.connector
import commands                         #   Para el uso de comandos Linux

class DataBase:

    __User          =   'root'
    __Password      =   '2010020726Ev'

    cnx             =   None
    cursor          =   None

    def __init__(self):

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                          host = '127.0.0.1',
                                          database = 'TablaRuteo')

            self.cursor = self.cnx.cursor()


            Agregar_Host = ("INSERT INTO Ruteo (Grupo, IP)"
                            "VALUES(%s, %s)")

            A = 'Grupo A'
            Ip = 'Shola'

            Host_me = (A, Ip)

            self.cursor.execute(Agregar_Host, Host_me)

            print("Se ha agregado una direccion")

            self.cnx.commit()
            self.cursor.close()



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

    #def Insertar(self):
