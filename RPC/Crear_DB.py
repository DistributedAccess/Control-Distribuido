from Create_DB import *

if __name__ == "__main__":

    passwd = input("Escribe la contrasena: ")
    str(passwd)
    x = Create_DB('root',passwd)

    x.Create_DataBase()
    x.Create_Ruteo()
    x.Create_Horario()
    x.Create_Bitacora()
    x.Create_Usuarios()
    x.Create_Laboratorio()

    x.Create_HorarioBB()
    x.Create_BitacoraBB()
    x.Create_UsuariosBB()
