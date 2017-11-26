from Control_Distribuido import *

class Servidor_Distribuido(Control_Distribuido):

    I_C = 1   #   Variable para el metodo Ingresar

    def __init__(self):
        Control_Distribuido.__init__(self, "Servidor")
        print("Constructor Servidor_Distribuido Listo!")

    def Ingresar(self, Ip, Grupo, Laboratorio):
        #   Este metodo se encarga de ingresar cualquier
        #   tipo de host al sistema distribuido, una vez
        #   dentro, regresara la tabla de ruteo al host.
        #
        #   Tambien se encarga de asignar al COORDINADOR
        #   este sera el primer host Cliente que se
        #   ingrese a la red.

        if (self.I_C == 1):
            self.Red.Agregar_Host(Ip,Grupo,Laboratorio,self.I_C)
            Replica = self.Red.Consultar("Ruteo")
            self.I_C = 0
        else:
            self.Red.Agregar_Host(Ip,Grupo,Laboratorio,self.I_C)
            Replica = self.Red.Consultar("Ruteo")

        return Replica
