
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

apo = argparse.ArgumentParser()
apo.add_argument('-i','--image', required = True, help = "Path to the image you wish to convolve")
args = vars(apo.parse_args())

def convolution(img, kernel):
    #adding padding to the image to not lose the spatial dimensions
    
    img_h, img_w = img.shape[:2]
    k_h, k_w = kernel.shape[:2]
    
    pad = (k_w - 1)//2
    
    #adding this padding to the image
    
    img = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    cv2.imshow("Image with padding",img)
    cv2.waitKey(0)

kernel = np.ones((3,3))
print(kernel)
img = cv2.imread(args["image"])
img = cv2.resize(img, (500,400))
convolution(img, kernel)   
    