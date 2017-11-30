from Configuracion_LBP import *
from picamera import PiCamera
from Procesamiento import *
from time import *


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
    camera.start_preview()

    for i in range(3):
        sleep(2)
        camera.capture('Imagen%s.jpg' % (i+1))

    camera.stop_preview()

def Capture():

    camera = PiCamera()
    camera.start_preview()

    sleep(2)
    camera.capture('Captura.jpg')

    camera.stop_preview()

def Reconocimiento():

    Proceso = Procesamiento()

    Imagen_Desco = Proceso.LBP('Captura.jpg')

    Proceso.Distancia_Euclidiana(Imagen_Desco)
