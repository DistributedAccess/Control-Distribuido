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

import math

class Procesamiento():

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

    def Distancia_Euclidiana(Imagen_Desconocida):
        """ Este metodo calcula la distancia euclidianana del LBP de la imagen
            desconocida con respecto a los LBP de cada usuario de la Base de
            Datos
        """

        #NoUsuarios = Numero_Usuarios()         OBTIENE EL NUMERO DE USUARIOS
        while (flag == 0):

            #Query = Consultar_Users(contador)

            for i in range (2):
                for j in range (15):

                    x = Imagen_Desconocida[j] - Query[i][j]
                    x = math.pow(x,2)

                    DE[i] = x + DE[i]

                DE[i] = math.sqrt(DE[i])
            if(DE[0] == DE[1] == DE[2]):
                flag = 1
                contador = 0
            else:
                flag = 1
                contador = contador + 1

            if(contador >= NoUsuarios):
                flag = 1
