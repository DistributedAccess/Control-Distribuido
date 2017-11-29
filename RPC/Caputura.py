from Configuracion_LBP import *
from picamera import PiCamera
from Procesamiento import *
from time import *


def Ingresar_al_Sistema(Boleta):

    LBPs = [None, None, None]
    Proceso = Procesamiento()
    Configu = Configuracion_LBP()

    Fotos()

    for i in range(3):
        LBPs[i] = LBP('Imagen%s.jpg' % (i+1))

    Configu.Asignar_LBP(Boleta, LBPs[0], LBP[1], LBP[2])

def Fotos():

    camera = PiCamera()
    camera.start_preview()

    for i in range(3):
        sleep(2)
        camera.capture('Imagen%s.jpg' % (i+1))

    camera.stop_preview()
