import commands

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
