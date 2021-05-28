## Implementing cross-correlation on images from scratch using Numpy

### Introduction
This is a numpy implementation to demonstrate the effect of applying cross-correlation between a kernel and an input image.

A kernel matrix __K__ of size _N x N_ (where N is odd) slides through an input image __I__ of size _P x Q_. (The kernel __K__ is a matrix smaller than that of image __I__).

An output matrix __O__ of the same size of image __I__ (i.e. _P x Q_) is initialized.

The center of kernel __K__ is placed at the __(x,y)__ coordinate of the image __I__. Following that, a local operation of __cross-correlation__ is applied. This operation simply performs an element-wise multiplcation between the kernel __K__ and the part of the image __I__ where kernel __K__ sits and then sums up all the values. The value thus received is known as the __kernel output__. This kernel output is stored at the __(x,y)__ cordinate of the matrix __O__.

This process is repeated for all the coordinates of image __I__. To maintain the original dimensions of the input image, extra layer(s) of padding is applied to the input image __I__. 


### Requirements 
* `numpy` to perform numerical computing. 
```
pip install numpy
```
* `scikit-image` to perform image proceessing.
```
pip install scikit-image
```
* `opencv` to display the images.
```
pip install opencv-python
```
### Running
Execute the following command to run the `correlation.py` file.
```
python correlation.py -- image images/test.jpg
```
It parses thorugh the command line argument `--image` which seeks the path of the image.

A number of kernels are already added in the script. To use a different kernel, add the kernel in the script and change the variable name while calling the `correlation` function. 

### Output
The following image demonstrates the output of the script (when run with various kernels). 
![Untitled — May 28, 12 08 56 PM](https://user-images.githubusercontent.com/30223211/119944606-173eaf00-bfb2-11eb-96bc-8c692dae651e.png)

_Expand and zoom over the images to distinguish the effect of the filters_

