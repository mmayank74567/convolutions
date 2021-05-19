
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

apo = argparse.ArgumentParser()
apo.add_argument('-i','--image', required = True, help = "Path to the image you wish to convolve")
args = vars(apo.parse_args())

def correlation(img, kernel):
    #adding padding to the image to not lose the spatial dimensions
    
    img_h, img_w = img.shape[:2]
    k_h, k_w = kernel.shape[:2]
    
    pad = (k_w - 1)//2
    
    #aaplying padding to the image
    
    img_pad = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    print("[INFORMATION] Padding on the input image has been applied")
    
    #creating an output matrix of the size of the image
    output = np.ones((img_h, img_w))
    
    #moving through the image and picking the region of interest
    #multiplying that by the kernel
    for i in range(0, img_h):
        for j in range(0, img_w):
            i = img_pad[i:k_h+i, j:k_w+j]
            value = (i*kernel).sum()
            output[img_h-1, img_w-1] = value
    
    #the output must have value between (0,255)
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    
    return output
    
kernel = np.ones((3,3))

img = cv2.imread(args["image"])
img = cv2.resize(img, (300,200))
c = correlation(img, kernel)   
cv2.imshow("Original Image", img)
cv2.imshow("After correlation", c)
cv2.waitKey(0)
cv2.destroyAllWindows()