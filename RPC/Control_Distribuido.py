from Configuracion_Red import *
import threading
import xmlrpclib
import Queue
import time

import xmlrpclib

class Control_Distribuido:

    Red      = None      #   Objeto de Configuracion_Red

    def __init__(self, Grupo):
        self.Red = Configuracion_Red(Grupo)
        print("Constructor Control_Distribuido Listo")

    def Replicacion(self, Grupo, Opcion):
        #   Replicacion solo responde a las solicitudes
        #   enviando asi las tablas solicitadas.
        #   Trabaja junto con Actualizar()
        Replica  = None      #   Variable de TABLA_RUTEO

        if (Grupo == "Servidor"):
            if (Opcion == "Ruteo"):
                Replica = self.Red.Consultar("Ruteo")
            elif (Opcion == "Total"):
                Replica = self.Red.Consultar("Total")
        elif (Grupo == "Cliente"):
            if (Opcion == "Ruteo"):
                Replica = self.Red.Consultar("Ruteo")
            elif (Opcion == "Replica"):
                Replica == self.Red.Consultar("Replica")

        return Replica

    def Actualizar(self, Grupo, Opcion, Data):
        #   Actualizar recibe las tablas de las
        #   bases de datos por parte de Replicacion()
        #   y de Ingresar()
        self.Red.Actualizar(Grupo,Opcion,Data)

    def Eleccion(self):
        print("Eleccion")
        return "OK"

    def Exclusion(self):
        print("Exclusion")
        return "OK"

    def Memoria_C(self):
        print("Memoria_C")
        return "OK"

    def Detec_Falla(self, Coordinador, Grupo):
        #   HAY DOS CASOS, CLIENTE-COORDINADOR Y
        #   COORDINADOR-CLIENTE, SOBRE CLIENTE-CLIENTE Y
        #   SERVIDOR-SERVIDOR

        if(Coordinador == 1):
        #   SIGNIFICA QUE MANDARA MENSAJES A SUS CLIENTES
            if(Grupo == "Servidor"):
                #   SERVIDOR-SERVIDOR
                Servidores = self.Red.Numero_Host("Servidor")#OBTIENE EL NUMERO DE SERVIDORES
                for Num_Hilo in range(Servidores):
                    Direccion = self.Red.Consultar_Ruta(Num_Hilo+1, "Servidor", 0)
                    hilo = threading.Thread(target=self.Hello,args=(Direccion,"2020",))
                    hilo.start()
            else:
                #   CLIENTE-CLIENTE
                Clientes = self.Red.Numero_Host("Cliente")#OBTIENE EL NUMERO DE CLIENTES
                for Num_Hilo in range(Clientes):
                    Direccion = self.Red.Consultar_Ruta(Num_Hilo+1, "Cliente", 0)
                    hilo = threading.Thread(target=self.Hello,args=(Direccion,"2020",))
                    hilo.start()
        else:
            #   MANDARA MENSAJES A SU COORDINADOR
            if(Grupo == "Servidor"):
                Direccion = Consultar_Ruta(1,"Servidor",1)
                Hello(Direccion,2018)
            else:
                Direccion = Consultar_Ruta(1,"Cliente",1)
                Hello(Direccion,2018)


    def Hello(self, Direccion, Puerto,  Periodo):
        #   Este metdo se encarga de mandar un mensaje de
        #   reconocimiento hello al host destino, si dicho
        #   host se encuentra conectado enviara un OK
        #   de otro modo no mandara nada y el algoritmo
        #   madara un mensaje de ERROR.

        Ip_Cliente = "http://"+Direccion+":"+Puerto
        Habla = xmlrpclib.ServerProxy(Ip_Cliente)

        cola = Queue.Queue()
        Contador = 0

        def Hello2():

            def Envia():
                try:
                    Respuesta = Habla.Transaccion("Hello")
                    cola.put(Respuesta)
                except Exception as error:
                    cola.put("ERROR")

            def Tiempo():
                time.sleep(Periodo - 0.2)

            Hilo1 = threading.Thread(target=Envia)
            Hilo2 = threading.Thread(target=Tiempo)

            #   El Hilo1 se configura como demonio, si el Hilo2 termina
            #   su ejecucion el Hilo1 se cerrara sin importar si Este
            #   sigue ejecutandose.
            Hilo1.setDaemon(True)

            Hilo1.start()
            Hilo2.start()

            time.sleep(Periodo)
            return cola.get()

        y = None
        while(Contador < 3):
            #   Este ciclo se encarga de enviar el mensaje Hello
            #   periodicamente hasta que haya una desconexion o un
            #   error, en caso de haberlo, el mensaje se enviara 3
            #   veces mas y en caso de no responder a dichos mensajes
            #   el programa retorna un mensaje de ERROR
            y = Hello2()

            if(y == "ERROR"):
                Contador = Contador + 1
            else:
                Contador = 0

        return y

    def Transaccion(self, Trans):
        #   FUNCION PARA RESPONDER A CUALQUIER TIPO DE MENSAJES

        if(Trans == "Hello"):
            #   Este if se usa cuando un CLIENTE o COORDINADOR
            #   externo desee supervisar la conexion con este
            #   host. De modo que si recibe un Hello este if
            #   responde con un OK
            return "OK"
