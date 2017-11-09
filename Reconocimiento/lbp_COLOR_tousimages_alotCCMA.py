#!/usr/bin/env python
# -*- coding: cp1252 -*-

__doc__ = """
Program for Colour Contrast Ocurrence (C2O) Matrix
Date: Mars 2014

Object : compute the vector contrast in CIElab at each location,
         between the 'x' location and a target location 'y'
         defined by a spatial distance and an angle (like cooccurrence).
         


At the start of main program you must define inside the source : 
                                        the path, 
                                        the filename and 
                                        the extension for the RGB file
fonctions :
    - fContrastMatrix   : To compute the vector contrast in CIELa
                            (using the skimage library and delta E calcul)
    - falpha    : to compute the angle alpha between L and delta (the contrast vector)
    - fgamma    : to compute the gamma angle inside the a and b plane
    - graphic3D : 3D plot of delta, alpha, gamma (classical orthornormal rep.)
                              this option disabled by comment (#)
    - fspherical3D : 3D plot in 3D spherical representation of delta,alpha,gamma 
                    this representation is the standard one for C2O
    - savematrix : to save the matrix in the .dat format for external analysis, 
                              this option disabled by comment (#)
                              
Comments :
    skimage.rgb2lab() function use the skimage.rgb2xyz() function based on
    a theoretical white reference coordinate : x=y=z=1/3, transform at :
     http://en.wikipedia.org/wiki/CIE_1931_color_space              
"""

from PIL import Image
import numpy as np
from skimage.color import deltaE_cie76
from skimage.color import rgb2gray
from skimage.color import rgb2xyz
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

 #####################

##===============================================================================
##        The call main
##===============================================================================

if __name__ == "__main__":
        #file_name ="d:/user/noel/Dropbox/Armando/images_database/Contrib_TC_00006/images/000000"
        #d:/ima/vistex/000144" # filepath + file name (without ext)
        #file_name="petite_bruit"
        #file_name="c:/data/ima/Outex_TC_00014/images/000272"
        #file_name="c:/data/ima/vistex/000258"

        #file_name="c:/Users/sears121/Pictures/alotsemi/207/207_c1l1r180"
        #C:\Users\sears121\Pictures\alotsemi\245
        #file_ext=".bmp"                   #  file extension
        
        
        #completed_file_name=file_name + file_ext # Joint the way and their extention
        #imat=Image.open(completed_file_name)
        #numima=7616 #for stex
        numima=4800
        way1="c:/data/ima/toustrain/"

        #way1="c:/data/ima/stexbonne/"
        ext=".png"
        nima=0
        conta=0
        neighbors=8
        radius=1
        n_points = 8 * radius
        METHOD = 'uniform'
        pfeat=np.zeros((numima,1530))
        #tot=np.zeros((1,765))
        #histo=np.zeros((1,255))
        #histo1=np.zeros((1,255))
        #histo2=np.zeros((1,255))
        for i2 in range (0,10):
                for i3 in range (0,10): 
                        for i4 in range (0,10):                             
                                nima=nima+1
                                wy4=str(nima)                               
                                waytot=way1+wy4+ext
                                imat=Image.open(waytot) #image way
                                
                               
                                for j1 in range (0,5):               
                                        for j2 in range (0,4):
                                                print conta
                                                x1=j1*128
                                                y1=j2*128
                                                box=[x1,y1,x1+128,y1+128]
                                                imas=imat.crop(box)                                                                
                                                arrayima=np.array(imas)
                        
                                                R = arrayima[:,:,0];
                                                G = arrayima[:,:,1];
                                                B = arrayima[:,:,2];
                                                spoints=np.zeros((neighbors,2))
                                                a = 2*np.pi/neighbors
                                                for i in range (0,neighbors-1):
                                                        spoints[i,0] = -1*radius*np.sin(i*a);
                                                        spoints[i,1] = radius*np.cos(i*a);
        

                                                miny=np.min(spoints[:,0])
                                                maxy=np.max(spoints[:,0])
                                                minx=np.min(spoints[:,1])
                                                maxx=np.max(spoints[:,1])

                                                bsizey=np.ceil(max(maxy,0))-np.floor(min(miny,0))+1;
                                                bsizex=np.ceil(max(maxx,0))-np.floor(min(minx,0))+1;
                                                origy=1-np.floor(min(miny,0))
                                                origx=1-np.floor(min(minx,0))

        # Calculate dx and dy;
                                                dx = len(arrayima) - bsizex-1
                                                dy = len(arrayima) - bsizey-1
                                                RC = B[origy:origy+dy,origx:origx+dx]
                                                RC2= R[origy:origy+dy,origx:origx+dx]
                                                RC3= G[origy:origy+dy,origx:origx+dx]
   # bins = 2**neighbors;

# Initialize the result matrix with zeros.
    #DeltaE=np.zeros((dy,dx))
                                                result=np.zeros(dy,dx);
                                                result2=np.zeros(dy,dx);
                                                result3=np.zeros(dy,dx);
                                                result4=np.zeros(dy,dx);
                                                result5=np.zeros(dy,dx);
                                                result6=np.zeros(dy,dx);

#Compute the LBP code image

                                                for i in range (0,neighbors-1):
                                                        y = spoints[i,0]+origy
                                                        x = spoints[i,1]+origx
        
# Calculate rounds for the x and y.
                                                        ry = np.round(y)
                                                        rx = np.round(x)
 
                                                        NG = B[ry:ry+dy,rx:rx+dx]
                                                        NG2= R[ry:ry+dy,rx:rx+dx]
                                                        NG3= G[ry:ry+dy,rx:rx+dx]
                                                        #NG4= R[ry:ry+dy,rx:rx+dx]
                                                        #NG5= G[ry:ry+dy,rx:rx+dx]
                                                        #NG6= G[ry:ry+dy,rx:rx+dx]
        
                                                        D = NG >= RC
                                                        D2 = NG2>= RC2
                                                        D3 = NG3>= RC3
                                                        D4 = NG >= RC2
                                                        D5 = NG>= RC3
                                                        D6 = NG2>= RC3
  
  #Update the result matrix.
                                                        v = 2**i
                                                        result = result + v*D
                                                        result2 = result2 + v*D2
                                                        result3 = result3 + v*D3
                                                        result4 = result4 + v*D4
                                                        result5 = result5 + v*D5
                                                        result6 = result6 + v*D6
  #  for i in DeltaE:
   #     print i
                                                histo=np.histogram(result,bins=255, range=(0,255))
                                                histo1=np.histogram(result2,bins=255, range=(0,255))
                                                histo2=np.histogram(result3,bins=255, range=(0,255))
                                                histo3=np.histogram(result,bins=255, range=(0,255))
                                                histo4=np.histogram(result2,bins=255, range=(0,255))
                                                histo5=np.histogram(result3,bins=255, range=(0,255))
                                                tot=np.concatenate((histo[0],histo1[0],histo2[0],histo3[0],histo4[0],histo5[0]),axis=0)
                                                #print tot
                                        #
                                                                             
    #pfeat[conta]=histo[0]
                                                pfeat[conta]=tot[:]
                                               # print pfeat
                                                conta+=1
                                                if (conta==numima):
                                                        break
                                        if (conta==numima):
                                                break
                                if (conta==numima):
                                        break
                        if (conta==numima):
                                break
                if (conta==numima):
                        break
#print pfeat
np.savetxt('c:/data/troisime_anne/resultados/lbp_ALOT_aptoula_train.dat',pfeat)


        #x=np.arange(




