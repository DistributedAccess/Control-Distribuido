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
   
    newMax  = 0 #number of patterns in the resulting LBP code
    index   = 0
  
    imag=Image.open ("c:/data/IMA/stexbonne/0.png")
    
    arrayima=np.array(imag)
   
    lbp=local_binary_pattern(arrayima[:,:,2], n_points, radius, METHOD)
   
    n_bins = int (lbp.max()-1)
    print n_bins
    his, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    print his
    hist(lbp,n_bins)
   
    show()

    

  


   
