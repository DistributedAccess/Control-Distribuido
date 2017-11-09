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


if __name__ == "__main__":

    radius = 2
    n_points = 8 * radius
    METHOD = 'uniform'
   # table = 0:2^samples-1
    newMax  = 0 #number of patterns in the resulting LBP code
    index   = 0
  #  imag=Image.open ("c:/data/ima/vistex/000800.bmp")
    #imag=Image.open ("c:/data/ima/vistex/000176.bmp")
   # imag=Image.open ("c:/data/IMA/outex_tc_00014/images/000272.bmp")
    imag=Image.open ("c:/data/IMA/stexbonne/0.png")
    #imag=Image.open ("c:/data/IMA/ima_Stex_Tree_0002_07.png")
   # imag=Image.open ("c:/data/IMA/alot110_c1l3.png")
    #imag=Image.open ("c:/data/IMA/maquillaje/Chanel/730ApMFc10.png")
    arrayima=np.array(imag)
   # imgray = rgb2gray(arrayima)
    lbp=local_binary_pattern(arrayima[:,:,2], n_points, radius, METHOD)
   # lbp=local_binary_pattern(imgray, n_points, radius, METHOD)
    n_bins = int (lbp.max()-1)
    print n_bins
    his, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
   # print his
    hist(lbp,n_bins)
   # print np.sum(hist)
   # plt.plot(n_bins,hist)
    show()

    
  #  plt.subplot(312)   
   # plt.plot(x,SIGalpha, color='blue', lw=3)
    #plt.ylabel('amplitud')
    #plt.title('alpha angle')

    #plt.subplot(313)   
    #plt.plot(x,SIGbeta,color='green', lw=3)
    #plt.ylabel('amplitud')
    #plt.title('beta angle')
    #plt.show()


  


   
