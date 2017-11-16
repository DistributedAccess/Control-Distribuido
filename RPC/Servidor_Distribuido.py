from Control_Distribuido import *

class Servidor_Distribuido(Control_Distribuido):

    def __init__(self):
        Control_Distribuido.__init__(self)
        print("Constructor SD")

    def Ingresar(self, Ip, Grupo):
        self.Red.Agregar_Host(Ip,Grupo)
        self.TB = self.Red.Consultar()

        return self.TB
