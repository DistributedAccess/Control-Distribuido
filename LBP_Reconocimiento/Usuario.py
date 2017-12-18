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

#   VARIABLES GLOBALES
Relay	  = 5
Boton_One = 6
Boton_Two = 13
Led_Red   = 19
Led_Green = 26

Estado_Boton = False

if __name__ == "__main__":

    #	ENTRENAMOS AL SISTEMA </3
    Entrenamiento()

    #	CONFIGURAMOS LA PICAMERA
    camera = PiCamera()
    camera.start_preview()
    #camera.rotation = 180
    camera.annotate_text_size = 80

    #	CONFIGURAMOS LOS GPIO
    GPIO.setmode(GPIO.BCM)		
    GPIO.setup(Relay,     GPIO.OUT)				# RELEVADOR
    GPIO.setup(Boton_One, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# BOTON ONE
    GPIO.setup(Boton_Two, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# BOTON TWO
    GPIO.setup(Led_Red,   GPIO.OUT)				# LED ROJO
    GPIO.setup(Led_Green, GPIO.OUT)				# LED VERDE

    try:

    	while(True):
	
	    Estado_Boton = GPIO.input(Boton_One)
	    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	    
	    GPIO.output(Led_Green, False)
            GPIO.output(Led_Red, True)
            GPIO.output(Relay, False)

	    if(Estado_Boton == True):

	    	Captura()
	    	Image = cv2.imread("Usuario.jpg")	
	    	Msg = Prediccion(Image)

	        if(Msg != 0):
		    camera.annotate_text = "Abierto"
		    GPIO.output(Led_Green, True)
		    GPIO.output(Led_Red, False)
		    GPIO.output(Relay, True)
		    Estado_Boton = False
		    sleep(10)

	    	elif(Msg == 0):
		    camera.annotate_text = "Cerrado"
		    GPIO.output(Led_Green, False)
		    GPIO.output(Led_Red, True)
                    GPIO.output(Relay, False)
		    Estado_Boton == False
		    sleep(1)
			
    except KeyboardInterrupt:
	GPIO.cleanup()
