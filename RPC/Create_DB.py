from mysql.connector import errorcode
import mysql.connector


class Create_DB:
    #   Esta clase se dedica a crear la base de datos
    #   y las tablas a usar en los servidores y en los
    #   procesos. Esta clase se ejecutara una sola vez
    #   solo en la instalacion de nuevos nodos.

    #   Variables privadas
    __User        =   'root'
    __Password    =   '2010020726Ev'
    __DB_NAME     =   'anina'
    #   Variables publicas
    cnx           =   None
    cursor        =   None

    def __init__(self, user, password):
        #   Esta funcion puede ser considerada como un
        #   constructor ya que cuando se instancia una clase
        #   esta se inicializa. Este constructor se conecta a
        #   la base de datos.
        self.U = user
        self.P = password

        #   Se actualizan las variables privadas para
        #   el inicio de sesion de la Base de Datos
        self.__User = user
        self.__Password = password

        #   Se conecta a la base de datos, si hay algun
        #   error en la conexion este te avisara.
        try:
            self.cnx = mysql.connector.connect(user = user, password = password)

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

    def Create_DataBase(self):

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password)
            self.cursor = self.cnx.cursor()

            SQL = "CREATE DATABASE IF NOT EXISTS anina"
            self.cursor.execute(SQL)
            print("Base de datos creada!")
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    def Create_Tables(self):

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                               host = '127.0.0.1',
                                               database = self.__DB_NAME)
            self.cursor = self.cnx.cursor()

            SQL = ("""CREATE TABLE IF NOT EXISTS Ruteo (
                    ID int(10) NOT NULL auto_increment,
                    Grupo varchar(100) NOT NULL,
                    IP varchar(16) NOT NULL,
                    PRIMARY KEY(ID)
                   )ENGINE=InnoDB;""")
            self.cursor.execute(SQL)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
