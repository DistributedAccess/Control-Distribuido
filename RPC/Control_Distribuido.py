from Configuracion_Red import *

class Control_Distribuido:

    Red = None
    TB  = None

    def __init__(self):
        self.Red = Configuracion_Red()
        print("Constructor CD")

    def Replicacion(self):
        print("Replicacion")
        return "OK"

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
