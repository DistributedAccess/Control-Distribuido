from Configuracion_LBP import *
from picamera import PiCamera
from Procesamiento import *
from time import *

#import numpy as np
#import cv2

def Ingresar_al_Sistema(Boleta):
    #   FUNCION QUE AGREGA AL USUARIO AL SISTEMA POR
    #   PRIMERA VEZ, O SE NECESITE ACTUALIZAR SUS LBP
    #   TRABAJA JUNTO CON Fotos()
    LBPs = [None, None, None]
    Proceso = Procesamiento()
    Configu = Configuracion_LBP()

    Fotos()

    for i in range(3):
        LBPs[i] = Proceso.LBP(('Imagen%s.jpg' % (i+1)))

    Configu.Asignar_LBP(Boleta, LBPs[0], LBPs[1], LBPs[2])

def Fotos():
    #   CAPTURA LAS FOTOGRAFIAS DEL USUARIO A INGRESAR
    #   AL SISTEMA
    camera = PiCamera()
    # camera.rotation = 180
    camera.start_preview()

    for i in range(3):
        sleep(2)
        camera.capture('Imagen%s.jpg' % (i+1))

    camera.stop_preview()

def Capture():

    camera = PiCamera()
    # camera.rotation = 180
    camera.start_preview()

    sleep(5)
    camera.capture('Captura.jpg')

    camera.stop_preview()

def Reconocimiento():

    Procesos = Procesamiento()

    Imagen_Desco = Procesos.LBP('Captura.jpg')

    Procesos.Distancia_Euclidiana(Imagen_Desco)

def Deteccion():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
