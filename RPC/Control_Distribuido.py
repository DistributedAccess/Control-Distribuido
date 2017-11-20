from Configuracion_Red import *

class Control_Distribuido:

    Red      = None      #   Objeto de Configuracion_Red
    Replica  = None      #   Variable de TABLA_RUTEO

    def __init__(self, Grupo):
        self.Red = Configuracion_Red(Grupo)
        print("Constructor CD")

    def Replicacion(self, Grupo, Opcion):
        #   Replicacion solo responde a las solicitudes
        #   enviando asi las tablas solicitadas.
        #   Trabaja junto con Actualizar()
        if (Grupo == "Servidor"):
            if (Opcion == "Ruteo"):
                self.Replica = self.Red.Consultar("Ruteo")
            elif (Opcion == "Total"):
                self.Replica = self.Red.Consultar("Total")
        elif (Grupo == "Cliente"):
            if (Opcion == "Ruteo"):
                self.Replica = self.Red.Consultar("Ruteo")
            elif (Opcion == "Replica"):
                self.Replica == self.Red.Consultar("Replica")

        return self.Replica

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

    def Detec_Falla(self):
        print("Detec_Falla")
        return "OK"
