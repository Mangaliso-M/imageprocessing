#author: Mangaliso M. Mngomezulu
#description: feature detection in biomedical images
#features can be used for detection

import imageio
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

#load the image
im  = imageio.imread('./datasets/rsna_hand_radiograph.png')

#this calculates the diffrence between values at the top and bottom, returning values far from 0 when there is a sudden change in intensity (horizontal, edge)
weights = [[1, 1, 1],
           [0, 0, 0],
           [-1,-1,-1]]

#convolve the image using the filter
edges = ndi.convolve(im, weights)

plt.imshow(edges, cmap='seismic') #new cmap value, better visualization of edges
plt.title('Edges From Hand X-Ray')
plt.show()

#sobel
#ndi.sobel(im, axis=0) #second param is orientation of the filter, 0 or 1 , H or V

edges0 = ndi.sobel(im, axis=0)
edges1 = ndi.sobel(im, axis=1)
edges = np.sqrt(np.square(edges0)+np.square(edges1)) #the distance
plt.imshow(edges, cmap='gray')
plt.title('Sobel filtered image, horizontal and vertical edge detection')
plt.show()