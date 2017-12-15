from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
import os

def Ingresar_al_Sistema(Id):
    
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    sleep(10)

    Dir = 1
    os.mkdir("Entrenamiento/U%s" % Dir)

    for i in range(12):
	sleep(2)
	camera.capture('Entrenamiento/U%s/Imagen%s.jpg' % (Dir, i+1))

    camera.stop_preview()
