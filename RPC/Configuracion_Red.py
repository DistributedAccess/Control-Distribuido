from mysql.connector import errorcode
import mysql.connector
import commands                         #   Para el uso de comandos Linux

class Configuracion_Red:

    #   Variables privadas
    _User        =   'root'
    _Password    =   '2010020726Ev'

    #   Variables publicas
    cnx         =   ''          #   Objeto para la Base de Datos
    Ip          =   ''          #   Direccion Ip
    Id          =   ''          #   Numero de Id
    Grupo       =   ''          #   Grupo del Host
    Tipo_Host   =   ''          #   Tipo de Host, Cliete o Servidor
    Coordinador =   ''          #   Bandera del Coordinador
    Busy        =   ''          #   Bnadera del estado

    def __init__(self, user, password):
        #   Esta funcion puede ser considerada como un
        #   constructor ya que cuando se instancia una clase
        #   esta se inicializa. Este constructor se conecta a
        #   la base de datos.
        self.U = user
        self.P = password

        #   Se actualizan las variables privadas para
        #   el inicio de sesion de la Base de Datos
        self._User = user
        self._Password = password

        #   Se conecta a la base de datos, si hay algun
        #   error en la conexion este te avisara.
        try:
            self.cnx = mysql.connector.connect(user = user, password = password,
                                          host = '127.0.0.1',
                                          database = 'TablaRuteo')
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

    def Conec_DB(self):
        #   Esta funcion conectara el objeto a la Base de datos
        #   por primera vez si no se han modificado las variables
        #   _User y _Password o cada que halla una desconexion
        #   hacia ella. Si el las variables _User y _Password
        #   fueron modficadas es necesario llamar a la funcion
        #   __init__(self, user, password)

        try:
            self.cnx = mysql.connector.connect(user = self._User, password = self._Password,
                                          host = '127.0.0.1',
                                          database = 'TablaRuteo')
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

    def Disco_DB(self):
        #   Esta funcion desconectara el objeto de la
        #   Base de datos.
        self.cnx.close()
        print("Desconexion de la Base de Datos")

    def Agregar(self):

        cursor = self.cnx.cursor()
        Agregar_Host = ("INSERT INTO Ruteo (Grupo, IP)"
                        "VALUES(%s, %s)")

        A = 'Grupo A'
        Ip = Ip_Host()

        Host_me = (A, Ip)

        cursor.execute(Agregar_Host, Host_me)

        print("Se ha agregado una direccion")

        self.cnx.commit()
        cursor.close()

    def Ip_Host():
        #   Esta funcion regresa la direccion ip del Host
        #   a traves de la libreria commands se ejecuta
        #   el programa hostname de Linux y lo que regresa
        #   se guarda en una variable para posteriormente
        #   separar la direccion que nos interesa

        Ip = commands.getoutput("hostname -I")
        Espacio = Ip.find(" ")
        Ip = Ip[0:Espacio]
        return Ip
