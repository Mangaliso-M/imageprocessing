#@author: Mangaliso M. Mngomezulu
#description: image resampling and interpolation

import imageio
import matplotlib.pyplot as plt
import numpy as np

#one image is used here owing to the absence of the main dataset, this is just meant to understand the code
#resampling increases or decreases the amount of space occupied by each pixel - its diffrent from croppin
im1 = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')
im2 = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')
im3 = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')

vol = np.stack([im1, im2, im3])

for image in vol:
    plt.imshow(image)
    plt.show()

