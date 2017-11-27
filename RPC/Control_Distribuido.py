from Configuracion_Red import *
import threading
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


    def Hello(self, Direccion, Puerto):
        #   La funcion Hello representa la estructura del algoritmo
        #   de deteccion de errores, el cual se basa en mandar un
        #   mensaje hello al host destino y esperar respuesta de
        #   parte de este, en caso de no haberla dentro del limite
        #   de tiempo se notificara un error hasta salir de esta
        #   funcion

        Ip_Cliente = "http://"+Direccion+":"+Puerto
        Habla = xmlrpclib.ServerProxy(Ip_Cliente)

        Contador = 0    # EL HELLO X4

        while(True):

            Respuesta = None
            Inicio = time.time()
            Fin = None

            while(Fin <= 5):
                Fin = time.time()
                Fin = Fin-Inicio

                if(Respuesta != "OK"):
                    #   ESTE IF SE ENCARGA DE ENVIAR LA
                    #   SOLICITUD DEL HELLO Y RECIBIR
                    #   RESPUESTA

                    Respuesta = Habla.Transaccion("Hello")
                    print(Respuesta, Ip_Cliente)

                else:
                    #   SI LA RESPUESTA HA SIDO IGUAL A "OK"
                    #   YA NO SE VULEVE A HACER UNA SOLICITUD
                    #   POR LO TANTO SE ESPERA A QUE TERMINE EL
                    #   TIEMPO LIMITE.
                    pass

            if(Respuesta == "OK"):
                    #   SI LA RESPUESTA FUE OK SE REINICIA EL
                    #   CONTADOR EN CASO DE TENER ALGUN DATO.
                    #   SE REINICIA EL ALGORITMOS DE DETECCION
                    #   DE ERRORES
                Contador = 0

            elif:
                    #   EN CASO DE NO HABER OBTENIDO RESPUESTA
                    #   SE INCREMENTA EN 1 AL CONTADOR Y EL
                    #   PROCESO VUELVE A COMENZAR
                    Contador = Contador + 1

            if(Contador > 3):
                    #   EL CONTADOR HA SUPERADO EL LIMITE DE
                    #   TRES DE MODO QUE QUE EL ALGORITMO SALE
                    #   DEL CICLO WHILE
                    print("ERRORSASO!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    break

    def Transaccion(self, Trans):
        #   FUNCION PARA RESPONDER A CUALQUIER TIPO DE MENSAJES

        if(Trans == "Hello"):
            #   Este if se usa cuando un CLIENTE o COORDINADOR
            #   externo desee supervisar la conexion con este
            #   host. De modo que si recibe un Hello este if
            #   responde con un OK
            return "OK"
