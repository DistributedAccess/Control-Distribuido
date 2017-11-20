from Control_Distribuido import *

class Servidor_Distribuido(Control_Distribuido):

    def __init__(self):
        Control_Distribuido.__init__(self, "Servidor")
        print("Constructor SD")

    def Ingresar(self, Ip, Grupo, Laboratorio):
        #   Este metodo se encarga de ingresar cualquier
        #   tipo de host al sistema distribuido, una vez
        #   dentro, regresara la tabla de ruteo al host.

        self.Red.Agregar_Host(Ip,Grupo,Laboratorio)
        Replica = self.Red.Consultar("Ruteo")

        return Replica
