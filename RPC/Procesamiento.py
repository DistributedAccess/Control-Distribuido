from PIL import Image
import numpy as np
from skimage.color import deltaE_cie76
from skimage.color import rgb2lab
from skimage.color import rgb2xyz
from skimage.color import rgb2gray
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pylab import hist, show

#BASES DE DATOS Y ASI
from Configuracion_LBP import *
import math

#OPEN CV
import sys, getopt
import cv2



class Procesamiento():

    Config = Configuracion_LBP()    #OBJETO DE CONFIGURACION

    def LBP(self, Imagen):
        """ Este metodo obtiene el Local Binary Pattern (LBP) de la Imagen
            de entrada y retorna su vector.
        """
        radius = 2
        n_points = 8 * radius
        METHOD = 'uniform'

        newMax  = 0 #number of patterns in the resulting LBP code
        index   = 0

        imag=Image.open (Imagen)

        arrayima=np.array(imag)

        lbp=local_binary_pattern(arrayima[:,:,2], n_points, radius, METHOD)

        n_bins = int (lbp.max()-1)
        his, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))

        return his

    def Distancia_Euclidiana(self, Imagen_Desconocida):
        """ Este metodo calcula la distancia euclidianana del LBP de la imagen
            desconocida con respecto a los LBP de cada usuario de la Base de
            Datos
        """
        NoUsuarios = self.Config.Numero_Usuarios()        # OBTIENE EL NUMERO DE USUARIOS
        DE = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]#Distancia Euclidiana
	contador = 1
	Usuario = 0
	y = 0	

	Prom = []

	print NoUsuarios
        while (contador <= NoUsuarios):

            Query = self.Config.Consultar_Usuarios(contador)

	    for i in range (10):

                for j in range (16):
                    x = round(Imagen_Desconocida[j],5) - round(Query[i][j],5)# Redondeamos a la Imagen de Desconocida 
		    x = math.pow(x,2)
                    y = x + y

                DE[i] = math.sqrt(y)
		y = 0		
		
	    #Obtiene el promedio de las distancias euclidanas con respecto a la
	    #imagen desconocida y lo guarda en un arreglo variable
	    Average = 0
	    Average = (DE[0]+DE[1]+DE[2])/10
	    Prom.append(Average)	
            print Average
	    contador = contador + 1
	
	anterior = 100
	for i in range(int(NoUsuarios)):
	    
	    if(Prom[i] < anterior):
		anterior = Prom[i]
		Usuario = i+1
	print "El Usuario: " ,Usuario
	Prom = 0

    def Deteccion(self, Imagen):
    	""" Este metodo detecta el rostro de la imagen de entrada y lo recorta
    guardando asi la imagen de entrada con el rostro a una resolucion de
  	    512x512 pixeles
        """
	def detect(img, cascade):
            rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
            if len(rects) == 0:
                return []
            rects[:,2:] += rects[:,:2]
            return rects


    	args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])

    	args = dict(args)
    	cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")

    	cascade = cv2.CascadeClassifier(cascade_fn)

    	img = cv2.imread(Imagen,cv2.IMREAD_COLOR)

    	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    	gray = cv2.equalizeHist(gray)

	rects = detect(gray, cascade)

    	crop_img = None
    	for x1, y1, x2, y2 in rects:
            crop_img = img[y1:y2, x1:x2]


    	newi = cv2.resize(crop_img,(512,512))    #REAJUSTAMOS LA IMAGEN
    	#cv2.imwrite('Recorte.jpg',newi)
        return newi
