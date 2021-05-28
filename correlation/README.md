## Implementing cross-correlation on images from scratch using Numpy

### Introduction
This code uses numpy to apply cross-correlation on images. 

#### Cross-correlation
It is the element wise multiplication of two matrices followed by a sum. 

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

The 3 x 3 is the default filter. To use a different kernel, add the kernel in the script and change the variable name while calling the `correlation` function. (A few 
other kernels are already added in the `correlation.py` script. 

### Output
The following image demonstrates the output of the script (when run with various kernels). 
