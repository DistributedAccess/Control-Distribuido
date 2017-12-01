'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

# local modules
#from video import create_capture
from common import clock, draw_str


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    #X1 = None
    #Y1 = None
    #X2 = None
    #Y2 = None

    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
	X1 = x1
	Y1 = y1
	X2 = x2
	Y2 = y2
		
    #crop_img = img[X1:Y1, X2:Y2]
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])

    args = dict(args)
    cascade_fn = args.get('--cascade', "haarcascade_frontalcatface_extended.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)

	
    img = cv2.imread('Gat.jpg',cv2.IMREAD_COLOR)	

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    rects = detect(gray, cascade)
    vis = img.copy()

    print (rects)	
    print (type(rects[0]))
    crop_img = None
    for x1, y1, x2, y2 in rects:
	crop_img = img[y1:y2, x1:x2]
    	cv2.imwrite('Recorte.jpg',crop_img)

    draw_rects(vis, rects, (0, 255, 0))
        
    cv2.imshow('facedetect', crop_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

