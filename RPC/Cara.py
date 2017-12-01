import sys, getopt
import numpy as np
import cv2

def Detec(Imagen):
    
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
    cv2.imwrite('Recorte.jpg',newi)
