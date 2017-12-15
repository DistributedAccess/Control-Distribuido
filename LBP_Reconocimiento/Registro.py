from picamera import PiCamera
from time import sleep
import numpy as np
import MySQLdb
import cv2
import os

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
			ID = %s"""

    cursor.execute(QUERY,[Numero])

    rows = cursor.fetchall()
    cursor.close()

    rows = str(rows)
    Comilla = rows.find("'")
    Coma = rows.find(",")
    rows = rows[Comilla+1:Coma-1]

    return rows


def Ingresar_al_Sistema(Dir):
    
    camera = PiCamera()
    #camera.rotation = 180
    camera.start_preview()
    #sleep(10)
    os.system("omxplayer Audios/Uno.mp3")
     
    os.mkdir("Entrenamiento/U%s" % Dir)

    for i in range(12):
        os.system("omxplayer Audios/%s.mp3" %(i+1))
	sleep(1.5)
	camera.capture('Entrenamiento/U%s/Imagen%s.jpg' % (Dir, i+1))
    
    os.system("omxplayer Audios/fin.mp3")

    camera.stop_preview()
