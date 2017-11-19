import MySQLdb
#   Esta clase se dedica a crear la base de datos y las tablas
#   a usar en los servidores y en los procesos. Esta clase se
#   ejecutara una sola vez solo en la instalacion de nuevos nodos.
#
#   La Base de Datos a crear tiene las siguientes caracteristicas:
#
#   Base de Datos:  CONTROL_DISTRIBUIDO
#   Tabla:          TABLA_RUTEO
#                   TABLA_REPLICADA
#
#   TABLA_RUTEO
#   +------------+------------------+------+-----+---------+----------------+
#   | Field      | Type             | Null | Key | Default | Extra          |
#   +------------+------------------+------+-----+---------+----------------+
#   | ID         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
#   | Process_ID | int(10)          | NO   |     | NULL    |                |
#   | IP         | varchar(16)      | NO   |     | NULL    |                |
#   | Grupo      | varchar(10)      | NO   |     | NULL    |                |
#   | Coordinador| BIT(1)           | NO   |     | NULL    |                |
#   | Busy       | BIT(1)           | NO   |     | NULL    |                |
#   +------------+------------------+------+-----+---------+----------------+
#
#   ID: Identificador de la llave primaria
#   Process_ID: Identificador del proceso Cliete o Servidor
#   IP: Direccion Ip del proceso Cliente o Servidor
#   Grupo: Clasifica a las direcciones Ip por Cliente o Servidor
#   Coordinador: Indica que Cliente y Servidor son coordinadores
#   Busy: Indica el estado ocupado/desocupado del Host
#
#
#   TABLA_REPLICADA
#   +------------+------------------+------+-----+---------+----------------+
#   | Field      | Type             | Null | Key | Default | Extra          |
#   +------------+------------------+------+-----+---------+----------------+
#
#

class Create_DB:

    #   Variables privadas
    __User        =   None
    __Password    =   None
    __DB_NAME     =   'CONTROL_DISTRIBUIDO'
    #   Variables publicas
    db            =   None
    cursor        =   None

    def __init__(self, user, password):
        #   Constructor de la clase, que  establece la conexion a
        #   la Base de Datos. Este constructor debe recibir el
        #   usuario y la contrasena del metodo o usuario que
        #   la este utilizando, debido a que el metodo que utilice
        #   esta clase ya cuenta con el usuario y la contrasena.

        self.U = user
        self.P = password

        #   Se actualizan las variables privadas para
        #   el inicio de sesion de la Base de Datos
        self.__User = user
        self.__Password = password

        self.db = MySQLdb.connect(user = user, passwd = password)
        print("Conexion establecida a la Base de Datos")

    def Create_DataBase(self):
        #   Este metodo crea la Base de Datos CONTROL_DISTRIBUIDO.
        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password)
        self.cursor = self.db.cursor()

        SQL = "CREATE DATABASE IF NOT EXISTS CONTROL_DISTRIBUIDO"
        self.cursor.execute(SQL)
        print("Base de Datos: CONTROL_DISTRIBUIDO creada!")

    def Create_Tables(self):
        #   Este metodo crea las Tablas: TABLA_RUTEO y
        #   TABLA_REPLICADA de la Base de Datos
        #   CONTROL_DISTRIBUIDO.


        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: TABLA_RUTEO
        SQL = ("""CREATE TABLE IF NOT EXISTS TABLA_RUTEO (
                Process_ID int(10) NOT NULL,
                IP varchar(16) NOT NULL,
                Grupo varchar(10) NOT NULL,
                Coordinador TINYINT(1) NOT NULL,
                Busy TINYINT(1) NOT NULL
               )ENGINE=InnoDB;""")

        self.cursor.execute(SQL)
        print("Tabla: TABLA_RUTEO creada!")
