#@Author: Mangaliso M. Mngomezulu
#Morphology: basic operations are dilation(expand the boundaries), erosion (decreases the image size by reducing boundary thickness)
# a structuring element is used to do the operations

from matplotlib.pyplot import plot
from skimage import morphology, data
from custom_lib import plot_comparison

#example skimage structuring element shapes
rectangle = morphology.rectangle(10,7) #width and height
square = morphology.square(3)


#example erosion
#define the image
image = data.horse()

#first define the structuring element
structuring_element = morphology.rectangle(10,4)

#perform the erosion using the built in methods
eroded_horse = morphology.binary_erosion(image, selem=structuring_element)

#display the image and it's eroded version #the images here apper to be swapped, fix this later.
plot_comparison(image, eroded_horse,"Eroded image") 

#dilation
dilated_horse = morphology.binary_dilation(image)

#display the results
plot_comparison(image, dilated_horse, "Dilated Horse")
