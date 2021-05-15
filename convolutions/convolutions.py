# -*- coding: utf-8 -*-
"""
Created on Fri May 14 09:00:37 2021

@author: HP
"""

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

#the convolve function

def convolve(img, kernel):
    #establishing the dimensions of the image and kernel
    (imgh, imgw) = img.shape[:2]
    (kerh, kerw) = kernel.shape[:2]
    
    #adding padding to the input image
    #so that the spatial size is not reduced
    
    padding = (kerw-1)//2
    
    img = cv2.copyMakeBorder(img, padding, padding, padding, padding, cv2.BORDER_REPLICATE)
    output = np.zeroes((imgh, imgw), dtype = "float32")
    
    