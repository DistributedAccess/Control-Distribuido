from picamera import PiCamera
from time import sleep
import numpy as np
import MySQLdb
import cv2
import os
import time

camera = PiCamera()

def Numero_Usuarios():
    """ Este metodo regresa el numero de usuarios """

    #   DECLARACION DE LOS OBJETOS DE LA BASE DE DATOS
    db = MySQLdb.connect(user = "root", passwd = "2010020726Ev",
                                host = '127.0.0.1',
                                db = 'CONTROL_DISTRIBUIDO')
    cursor = db.cursor()

    QUERY = """SELECT count(ID) FROM USUARIOS"""

    cursor.execute(QUERY)

    rows = cursor.fetchall()
    cursor.close()

    rows = str(rows[0])
    rows = rows.translate(None,"(L,)")
    rows = float(rows)
    return rows

def Usuario_No(Numero):
    """ Este metodo regresa el nombre del usuario"""

    #   DECLARACION DE LOS OBJETOS DE LA BASE DE DATOS
    db = MySQLdb.connect(user = "root", passwd = "2010020726Ev",
                                host = '127.0.0.1',
                                db = 'CONTROL_DISTRIBUIDO')
    cursor = db.cursor()

    QUERY = """SELECT Nombre FROM USUARIOS WHERE 
			ID = %s AND LBP_1 IS NULL"""

    cursor.execute(QUERY,[Numero])

    rows = cursor.fetchall()
    cursor.close()

    rows = str(rows)
    Comilla = rows.find("'")
    Coma = rows.find(",")
    rows = rows[Comilla+1:Coma-1]

    return rows


def Captura(Dir, i):
    
    camera.capture('Entrenamiento/U%s/Imagen%s.jpg' % (Dir, i+1))
    try:
        Image = cv2.imread('Entrenamiento/U%s/Imagen%s.jpg' % (Dir, i+1))
        camera.annotate_text = "Detectando rostro"
        Deteccion_Rostro(Image)
        return "Ok"

    except IndexError:
        Captura(Dir, i)


def Ingresar_al_Sistema(Dir):

    #camera = PiCamera()
    #camera.rotation = 180
    camera.start_preview()
    
    os.system("omxplayer Audios/Uno.mp3")
     
    os.mkdir("Entrenamiento/U%s" % Dir)

    for i in range(12):
        os.system("omxplayer Audios/%s.mp3" %(i+1))
	sleep(1.5)

	Captura(Dir, i)
	#camera.capture('Entrenamiento/U%s/Imagen%s.jpg' % (Dir, i+1))
    
    os.system("omxplayer Audios/fin.mp3")

    #camera.stop_preview()



if __name__ == "__main__":

    Usuarios = Numero_Usuarios()
    Usuarios = int(Usuarios)


    print "\n			Bienvenido!!!!"
    print "\n	Los Usuarios que se demuestran a continuacion no se"
    print "	encuentran sus fotografias en la Base de Datos. Favor"
    print "        de escribir el numero del usuario para registrarlo."
    
    for i in range(Usuarios):
	User = Usuario_No(i + 1)
	if (User != ""):
	    print i+1, User

    usuario = raw_input("\n	Introduzca el Numero del Usuario: ")
    
    inicio_usuario = time.time()	#    TIEMPO DE INGRESAR AL SISTEMA
    Ingresar_al_Sistema(usuario)	#    
    fin_usuario = time.time()		#
    tiempo = fin_usuario-inicio_usuario	#
    print tiempo			#
