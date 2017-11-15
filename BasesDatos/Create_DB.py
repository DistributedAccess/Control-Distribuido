from mysql.connector import errorcode
import mysql.connector


class Create_DB:
    #   Esta clase se dedica a crear la base de datos y las tablas
    #   a usar en los servidores y en los procesos. Esta clase se
    #   ejecutara una sola vez solo en la instalacion de nuevos nodos.
    #
    #   La Base de Datos a crear tiene las siguientes caracteristicas:
    #
    #   Base de Datos:  CONTROL_DISTRIBUIDO
    #   Tabla:          TABLA_RUTEO
    #
    #   +------------+------------------+------+-----+---------+----------------+
    #   | Field      | Type             | Null | Key | Default | Extra          |
    #   +------------+------------------+------+-----+---------+----------------+
    #   | ID         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    #   | Process_ID | int(10)          | NO   |     | NULL    |                |
    #   | IP         | varchar(16)      | NO   |     | NULL    |                |
    #   | Grupo      | varchar(10)      | NO   |     | NULL    |                |
    #   | Coordinador| BIT(1)           | NO   |     | NULL    |                |
    #   | Bussy      | BIT(1)           | NO   |     | NULL    |                |
    #   +------------+------------------+------+-----+---------+----------------+
    #
    #   ID: Identificador de la llave primaria
    #   Process_ID: Identificador del proceso Cliete o Servidor
    #   IP: Direccion Ip del proceso Cliente o Servidor
    #   Grupo: Clasifica a las direcciones Ip por Cliente o Servidor
    #   Coordinador: Indica que Cliente y Servidor son coordinadores
    #   Bussy: Indica el estado ocupado/desocupado del Host


    #   Variables privadas
    __User        =   'root'
    __Password    =   '2010020726Ev'
    __DB_NAME     =   'CONTROL_DISTRIBUIDO'
    #   Variables publicas
    cnx           =   None
    cursor        =   None

    def __init__(self):
        #   Esta funcion puede ser considerada como un
        #   constructor ya que cuando se instancia una clase
        #   esta se inicializa. Este constructor se conecta a
        #   la base de datos.

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password)
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

            SQL = "CREATE DATABASE IF NOT EXISTS CONTROL_DISTRIBUIDO"
            self.cursor.execute(SQL)
            print("Base de Datos: CONTROL_DISTRIBUIDO creada!")
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    def Create_Tables(self):

        try:
            self.cnx = mysql.connector.connect(user = self.__User, password = self.__Password,
                                               host = '127.0.0.1',
                                               database = self.__DB_NAME)
            self.cursor = self.cnx.cursor()

            SQL = ("""CREATE TABLE IF NOT EXISTS TABLA_RUTEO (
                    ID int(10) NOT NULL auto_increment,
                    Process_ID int(10) NOT NULL,
                    IP varchar(16) NOT NULL,
                    Grupo varchar(10) NOT NULL,
                    Coordinador BIT(1) NOT NULL,
                    Bussy BIT(1) NOT NULL,
                    PRIMARY KEY(ID)
                   )ENGINE=InnoDB;""")
            self.cursor.execute(SQL)
            print("Tabla: TABLA_RUTEO creada!")
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
