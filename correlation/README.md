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

A number of kernels are already added in the script. To use a different kernel, add the kernel in the script and change the variable name while calling the `correlation` function. 

### Output
The following image demonstrates the output of the script (when run with various kernels). 
![Untitled — May 28, 12 08 56 PM](https://user-images.githubusercontent.com/30223211/119944606-173eaf00-bfb2-11eb-96bc-8c692dae651e.png)

_Expand and zoom over the images to distinguish the effect of the filters_

