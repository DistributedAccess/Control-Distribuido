from Configuracion_Red import *
import threading
import time

import xmlrpclib

class Control_Distribuido:

    Red      = None      #   Objeto de Configuracion_Red

    def __init__(self, Grupo):
        self.Red = Configuracion_Red(Grupo)
        print("Constructor CD")

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

    def Detec_Falla(self, Coordinador,Hello):

        if(Hello == "Hello"):
            #   Este if se usa cuando un CLIENTE o COORDINADOR
            #   externo desee supervisar la conexion con este
            #   host. De modo que si recibe un Hello este if
            #   responde con un OK
            return "OK"

        if(Coordinador == 1)

            Contador = 0
            while(True):

                Respuesta = None
                Inicio = time.time()
                Fin = None

                while(Fin <= 5):
                    Fin = time.time()
                    Fin = Fin-Inicio

                    if(Respuesta == "OK"):
                        #   ESTE IF SE ENCARGA DE ENVIAR LA
                        #   SOLICITUD DEL HELLO Y RECIBIR
                        #   RESPUESTA
                        pass

                    else:
                        #   SI LA RESPUESTA HA SIDO IGUAL A "OK"
                        #   YA NO SE VULEVE A HACER UNA SOLICITUD
                        #   POR LO TANTO SE ESPERA A QUE TERMINE EL
                        #   TIEMPO LIMITE.
                        pass

                if(Respuesta == "OK")
                        #   SI LA RESPUESTA FUE OK SE REINICIA EL
                        #   CONTADOR EN CASO DE TENER ALGUN DATO.
                        #   SE REINICIA EL ALGORITMOS DE DETECCION
                        #   DE ERRORES
                    Contador = 0

                if(Contador < 3):
                        #   EN CASO DE NO HABER OBTENIDO RESPUESTA
                        #   SE INCREMENTA EN 1 AL CONTADOR Y EL
                        #   PROCESO VUELVE A COMENZAR
                        Contador = Contador + 1
                else:
                        #   EL CONTADOR HA SUPERADO EL LIMITE DE
                        #   TRES DE MODO QUE QUE EL ALGORITMO SALE
                        #   DEL CICLO WHILE
                        break
