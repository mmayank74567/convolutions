
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
    
    #applying padding to the image
    img_pad = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    
    #creating an output matrix of the size of the image
    output = np.ones((img_h, img_w), dtype = "float32")
    
    #moving through the image and picking the region of interest
    #multiplying that by the kernel
    for i in range(0, img_h):
        for j in range(0, img_w):
            overlap_img = img_pad[i:k_h+i, j:k_w+j]          
            value = (overlap_img*kernel).sum()
            output[i, j] = value
    
    #the output must have value between (0,255)
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
     
    return output

#kernel to appy mean average
kernel = np.ones((3,3), dtype = "float32")
kernel = kernel / 9

#kernel to sharpen the image
sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")


sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")


img1 = cv2.imread(args["image"])
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(img1, (400,300))

#change the kernel variable in the next function according to the need
crr = correlation(img1, sharpen)

cv2.imshow("Original Image", img1)
cv2.imshow("Image", crr)

cv2.waitKey(0)
cv2.destroyAllWindows()