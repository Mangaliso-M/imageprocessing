#@author: Mangaliso M. Mngomezulu
#spatial transformations
#Dataset: Open Access Series Of Imaging Studies
#Lecture Notes
#mock data was used instead of OASIS

"""
registration - the process of aligning two images together.
             - this requires rotating, translating & scaling the images.
"""

import imageio
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage import color

#load the image
#im = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')
#plt.imshow(im)
#plt.show()

"""
 centering an image
    - get the shape of the image, that will be (x,y) whei is for dimensions of the image
    - get the center (x/2, y/2) = (xc, yc)
    - get the center of mass of the image (cmx, cmy)
    - then compute the center location of the image, as:
                center = (xc, xy) - (cmx, cmy)
    - call the shift function to shift the image's center of mass to the new location
"""
im = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')

#just for formality, ensure that the image is in grayscale
im = color.rgb2gray(im)

#print('Image shape:',im.shape)
x , y = im.shape
x /= 2
y /= 2

#get the center of mass
com = ndi.center_of_mass(im)

d0 = x - com[0]
d1 = x - com[1]

#last step
xfm = ndi.shift(im, shift=[d0, d1])


#rotation can be performed similary, using the rotate function
xfm = ndi.rotate(im, angle=30, axes=(0,1))

#the rotates image may be bad, add the reshape argument and set it to false so that everything is on scale
xfm = ndi.rotate(im, angle = 30, reshape=False)


"""
 In the case of complex transformations, it is useful to compute a transformation matrix for the image 
 - the transformation matrix elements have instructions for the functions described above

"""
#the identity matrix will return the same image  it received as a param
mat = [[1,0,0],[0,1,0],[0,0,1]]

def printMatrix(matrix):
    for row in matrix:
        print('|',str(row).replace('[','').replace(']',''),'|')

xfm = ndi.affine_transform(im, mat)

plt.imshow(xfm)
plt.show()