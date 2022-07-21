#@author: Mangaliso M. Mngomezulu
#@descrip: Convolutions - feature finder

#example and edge where values go from 0 to 1
#the convolved edge is always emphasized
from curses import window
import numpy as np

array = np.array([0,0,0,0,0,1,1,1,1,1]) #edge 0 , 1
kernel = np.array([-1,1]) #detects an edge of change in values from high to low

#result
conv = np.array([0,0,0,0,0,0,0,0,0,0])

for i in range(len(array) - 2):
    conv[i] = (kernel * array[i:i+2]).sum()

#assume an image is defined as image, then a kernel for detecting vertical changes is defined and used

kernel = np.array([[-1,1]
                  ,[-1,1]])

image = [[0,0],[0,0]] #for this example the image has to be a 27 x 27

conv = np.zeros(27, 27)

for i in range(27):
    for j  in range(27):
        window = image[i:i+2, j:j+2]
        conv[i,j] = np.sum(window * kernel)

