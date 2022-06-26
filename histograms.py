#@Author: Mangaliso Mngomezulu
#view images from the perspective of histograms

from skimage import data, io
import numpy as np
import matplotlib.pyplot as plt

#load the image from the skimage library
astronout = data.astronaut()

#original image
io.imshow(astronout)
plt.title("Original Astronout image")
plt.show()

#pick the red layer of the image 
red = astronout[:,:,0] #the first of the three, in the 3rd dimension

#pick the green layer of the image
green  = astronout[:,:,1]  #green is the second of 3 layers of the image in the 3rd dimension

#pick the blue layer of the image
blue  = astronout[:,:,2] #blue is the last of the three

#put them in an array for display
images = [[red,"red"], [green,"green"], [blue,"blue"]] 

for image in images:
    io.imshow(image[0])
    plt.title(image[1])
    plt.show()

#similary with the display above, show the histograms
#ravel() to returns a continous flatterned array
#bins - 0 - 255
for image in images:
    plt.hist(image[0].ravel(), bins=256)
    plt.title(image[1])
    plt.show()
