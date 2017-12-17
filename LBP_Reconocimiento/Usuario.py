from Procesamiento import *
import RPi.GPIO as GPIO
from picamera import *
import datetime as dt
from time import *
import cv2

def Captura():
    camera.annotate_text = "Capturando ..."
    sleep(3)
    camera.capture("Usuario.jpg")
    try:
	Image = cv2.imread("Usuario.jpg")
	camera.annotate_text = "Detectando rostro"
    	Deteccion_Rostro(Image)
    	return "Ok"

    except IndexError:
	Captura()

Boton = True

if __name__ == "__main__":

    #    ENTRENAMOS AL SISTEMA </3
    Entrenamiento()

    camera = PiCamera()
    camera.start_preview()
    camera.rotation = 180
    #camera.brightness = 75
    camera.annotate_text_size = 80


    while(True):
	#camera.annotate_text = "Presione el Boton"
	camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	if(Boton == True):
	    Captura()
	    Image = cv2.imread("Usuario.jpg")	
	    print type(Image)
	    Msg = Prediccion(Image)
	    print Msg
	    Boton = True
