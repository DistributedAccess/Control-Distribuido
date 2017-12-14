import MySQLdb
"""   Esta clase se dedica a crear la base de datos y las tablas
      a usar en los servidores y en los procesos. Esta clase se
      ejecutara una sola vez solo en la instalacion de nuevos nodos.

      La Base de Datos a crear tiene las siguientes caracteristicas:

      Base de Datos:  CONTROL_DISTRIBUIDO

      Tablas:         TABLA_RUTEO
                      USUARIOS
                      BITACORA
                      LABORATORIO
                      HORARIO
                      HORARIOBB
                      USUARIOSBB
                      BITACORABB

      TABLA_RUTEO
      +------------+------------------+------+-----+---------+----------------+
      | Field      | Type             | Null | Key | Default | Extra          |
      +------------+------------------+------+-----+---------+----------------+
      | Process_ID | int(10)          | NO   |     | NULL    |                |
      | Laboratorio| varchar(16)      | NO   |     | NULL    |                |
      | IP         | varchar(16)      | NO   |     | NULL    |                |
      | Grupo      | varchar(10)      | NO   |     | NULL    |                |
      | Coordinador| TINYINT(1)       | NO   |     | NULL    |                |
      +------------+------------------+------+-----+---------+----------------+

      USUARIOS
      +-----------+-------------+------+-----+---------+-------+
      | Field     | Type        | Null | Key | Default | Extra |
      +-----------+-------------+------+-----+---------+-------+
      | ID        | int(10)     | NO   | PRI | NULL    |       |
      | Nombre    | varchar(50) | NO   |     | NULL    |       |
      | Password  | varchar(10) | NO   |     | NULL    |       |
      | Jerarquia | varchar(10) | NO   |     | NULL    |       |
      | LBP_1     | tinytext    | NO   |     | NULL    |       |
      | LBP_2     | tinytext    | NO   |     | NULL    |       |
      | LBP_3     | tinytext    | NO   |     | NULL    |       |
      +-----------+-------------+------+-----+---------+-------+

      BITACORA
      +--------------+-------------+------+-----+---------+-------+
      | Field        | Type        | Null | Key | Default | Extra |
      +--------------+-------------+------+-----+---------+-------+
      | Nombre       | varchar(50) | NO   |     | NULL    |       |
      | Laboratorio  | int(10)     | NO   |     | NULL    |       |
      | Hora_Entrada | datetime    | NO   |     | NULL    |       |
      +--------------+-------------+------+-----+---------+-------+

      LABORATORIO
      +--------+-------------+------+-----+---------+-------+
      | Field  | Type        | Null | Key | Default | Extra |
      +--------+-------------+------+-----+---------+-------+
      | ID_Lab | int(10)     | NO   | PRI | NULL    |       |
      | Ip     | varchar(16) | NO   |     | NULL    |       |
      +--------+-------------+------+-----+---------+-------+

      HORARIO
      +-------------+-------------+------+-----+---------+-------+
      | Field       | Type        | Null | Key | Default | Extra |
      +-------------+-------------+------+-----+---------+-------+
      | Nombre      | varchar(50) | NO   |     | NULL    |       |
      | Laboratorio | int(10)     | NO   |     | NULL    |       |
      | Grupo       | varchar(8)  | NO   |     | NULL    |       |
      | Hora        | time        | NO   |     | NULL    |       |
      | Dia         | varchar(8)  | NO   |     | NULL    |       |
      +-------------+-------------+------+-----+---------+-------+

      HORARIOBB
      +--------+-------------+------+-----+---------+-------+
      | Field  | Type        | Null | Key | Default | Extra |
      +--------+-------------+------+-----+---------+-------+
      | Nombre | varchar(50) | NO   |     | NULL    |       |
      | Grupo  | varchar(8)  | NO   |     | NULL    |       |
      | Hora   | time        | NO   |     | NULL    |       |
      | Dia    | varchar(8)  | NO   |     | NULL    |       |
      +--------+-------------+------+-----+---------+-------+

      UsuariosBB
      +-----------+-------------+------+-----+---------+-------+
      | Field     | Type        | Null | Key | Default | Extra |
      +-----------+-------------+------+-----+---------+-------+
      | Nombre    | varchar(50) | NO   |     | NULL    |       |
      | Password  | varchar(10) | NO   |     | NULL    |       |
      | Jerarquia | varchar(10) | NO   |     | NULL    |       |
      | LBP_1     | tinytext    | NO   |     | NULL    |       |
      | LBP_2     | tinytext    | NO   |     | NULL    |       |
      | LBP_3     | tinytext    | NO   |     | NULL    |       |
      +-----------+-------------+------+-----+---------+-------+

      BITACORABB
      +--------------+-------------+------+-----+---------+-------+
      | Field        | Type        | Null | Key | Default | Extra |
      +--------------+-------------+------+-----+---------+-------+
      | Nombre       | varchar(50) | NO   |     | NULL    |       |
      | Hora_Entrada | datetime    | NO   |     | NULL    |       |
      +--------------+-------------+------+-----+---------+-------+
"""

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

    def Create_Ruteo(self):
        #   Este metodo crea la Tabla: TABLA_RUTEO
        #   de la Base de Datos CONTROL_DISTRIBUIDO.

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: TABLA_RUTEO
        QUERY = ("""CREATE TABLE IF NOT EXISTS TABLA_RUTEO (
                    Process_ID int(10) NOT NULL,
                    Laboratorio varchar(16) NOT NULL,
                    IP varchar(16) NOT NULL,
                    Grupo varchar(10) NOT NULL,
                    Coordinador TINYINT(1) NOT NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: TABLA_RUTEO creada!")

    def Create_Usuarios(self):
        #   Este metodo crea la Tabla: USUARIOS
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: USUARIOS
        QUERY = ("""CREATE TABLE IF NOT EXISTS USUARIOS (
                    ID int(10) NOT NULL,
                    Nombre varchar(50) NOT NULL,
                    Password varchar(10) NULL,
                    Jerarquia varchar(10) NULL,
                    LBP_1 TEXT(100) NULL,
                    LBP_2 TEXT(100) NULL,
                    LBP_3 TEXT(100) NULL,
		    LBP_4 TEXT(100) NULL,
		    LBP_5 TEXT(100) NULL,
		    LBP_6 TEXT(100) NULL,
		    LBP_7 TEXT(100) NULL,
		    LBP_8 TEXT(100) NULL,
		    LBP_9 TEXT(100) NULL,
		    LBP_10 TEXT(100) NULL,
                    PRIMARY KEY (ID)
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: USUARIOS creada!")

    def Create_Bitacora(self):
        #   Este metodo crea la Tabla: BITACORA
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: BITACORA
        QUERY = ("""CREATE TABLE IF NOT EXISTS BITACORA (
                    Nombre varchar(50) NOT NULL,
                    Laboratorio int(10) NOT NULL,
                    Hora_Entrada DATETIME NOT NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: BITACORA creada!")

    def Create_Laboratorio(self):
        #   Este metodo crea la Tabla: LABORATORIO
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: LABORATORIO
        QUERY = ("""CREATE TABLE IF NOT EXISTS LABORATORIO (
                    ID_Lab int(10) NOT NULL,
                    Ip varchar(16) NOT NULL,
                    PRIMARY KEY (ID_Lab)
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: LABORATORIO creada!")

    def Create_Horario(self):
        #   Este metodo crea la Tabla: HORARIO
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: HORARIO
        QUERY = ("""CREATE TABLE IF NOT EXISTS HORARIO (
                    Nombre varchar(50) NOT NULL,
                    Laboratorio int(10) NOT NULL,
                    Grupo varchar(8) NOT NULL,
                    Hora TIME NOT NULL,
                    Dia varchar (8) NOT NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: HORARIO creada!")

    def Create_HorarioBB(self):
        #   Este metodo crea la Tabla: HORARIOBB
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: HORARIOBB
        QUERY = ("""CREATE TABLE IF NOT EXISTS HORARIOBB (
                    Nombre varchar(50) NOT NULL,
                    Grupo varchar(8) NOT NULL,
                    Hora TIME NOT NULL,
                    Dia varchar (8) NOT NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: HORARIOBB creada!")

    def Create_UsuariosBB(self):
        #   Este metodo crea la Tabla: USUARIOSBB
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: USUARIOSBB
        QUERY = ("""CREATE TABLE IF NOT EXISTS USUARIOSBB (
                    Nombre varchar(50) NOT NULL,
                    Password varchar(10) NOT NULL,
                    Jerarquia varchar(10) NOT NULL,
                    LBP_1 TEXT(100) NULL,
                    LBP_2 TEXT(100) NULL,
                    LBP_3 TEXT(100) NULL,
		    LBP_4 TEXT(100) NULL,
                    LBP_5 TEXT(100) NULL,
                    LBP_6 TEXT(100) NULL,
                    LBP_7 TEXT(100) NULL,
                    LBP_8 TEXT(100) NULL,
                    LBP_9 TEXT(100) NULL,
                    LBP_10 TEXT(100) NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: USUARIOSBB creada!")

    def Create_BitacoraBB(self):
        #   Este metodo crea la Tabla: BITACORA
        #   de la Base de Datos CONTROL_DISTRIBUIDO

        self.db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                                        host = '127.0.0.1',
                                        db = self.__DB_NAME)

        self.cursor = self.db.cursor()

        #   Creacion de la tabla: BITACORA
        QUERY = ("""CREATE TABLE IF NOT EXISTS BITACORABB (
                    Nombre varchar(50) NOT NULL,
                    Hora_Entrada DATETIME NOT NULL
                    )ENGINE=InnoDB;""")

        self.cursor.execute(QUERY)
        print("Tabla: BITACORABB creada!")
