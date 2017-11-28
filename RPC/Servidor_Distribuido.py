from Control_Distribuido import *

class Servidor_Distribuido(Control_Distribuido):

    I_C = 1   #   Variable para el metodo Ingresar

    def __init__(self):
        Control_Distribuido.__init__(self, "Servidor")
        print("Constructor Servidor_Distribuido Listo!")

    def Ingresar(self, Ip, Grupo, Laboratorio):
        #   Este metodo se encarga de ingresar cualquier
        #   tipo de host al sistema distribuido, una vez
        #   dentro, regresara la tabla de ruteo al host
        #   y actualizara la tabla de ruteo de todos los
        #   otros hosts.
        #
        #   Tambien se encarga de asignar al COORDINADOR
        #   este sera el primer host Cliente que se
        #   ingrese a la red.

        if (self.I_C == 1):
            self.Red.Agregar_Host(Ip,Grupo,Laboratorio,self.I_C)
            Replica = self.Red.Consultar("Ruteo")
            self.I_C = 0
        else:
            self.Red.Agregar_Host(Ip,Grupo,Laboratorio,self.I_C)#EL SERVIDOR AGREGA UN HOST EXTERNO
            Replica = self.Red.Consultar("Ruteo")#EL SERVIDOR CONSULTA S NUEVA TABLA DE RUTEO Y LA REPLICA

            #   ENVIA A TODOS LOS HOST SERVIDOR LA NUEVA TABLA DE RUTEO
            Servidores = self.Red.Numero_Host("Servidor")#OBTIENE EL NUMERO DE SERVIDORES
            print "SERVIDORES: ", Servidores
            if(Servidores > 1):
                for Nu in range(2, Servidores+1):
                    Direccion = self.Red.Consultar_Ruta(Nu, "Servidor", 0)
                    Ip_Cliente = "http://"+Direccion+":"+"2027"
                    Habla = xmlrpclib.ServerProxy(Ip_Cliente)
                    Habla.Actualizar("Servidor","Ruteo",Replica)
                    print ("Se ha actualizado: ", Direccion)
            #   ENVIA A TODOS LOS HOST CLIENTE LA NUEVA TABLA DE RUTEO
            Clientes = self.Red.Numero_Host("Cliente")#OBTIENE EL NUMERO DE CLIENTES
            print "CLIENTES: ", Clientes
            if(Clientes > 1):
                for Nu in range(2, Clientes+1):
                    Direccion = self.Red.Consultar_Ruta(Nu, "Cliente", 0)
                    Ip_Cliente = "http://"+Direccion+":"+"2027"
                    Habla = xmlrpclib.ServerProxy(Ip_Cliente)
                    Habla.Actualizar("Cliente","Ruteo",Replica)
                    print("Se ha actualizado: ", Direccion)

        return Replica #ENVIA LA REPLICA AL HOST QUE RECIEN INGRESO
