#author: Mangaliso
#descrip: Smoothing and sharpening
"""
make use of kernels, they can move across the image to affect pixels
the kernel is used in the convolution to affect individual pixels of the parent matrix
"""


import imageio
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

im = imageio.imread('./datasets/rsna_hand_radiograph.png')

random_weights = [[.15, .15, .15],
                  [.15, .7, .15],
                  [.15, .15, .15]]

filtered_image = ndi.convolve(im, random_weights)

fig, axes = plt.subplots(2,1)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(filtered_image, cmap='gray')
plt.show()

"""
Other functions that can be used on filtering
median_filter()
uniform_filter()
maximum_filter()
percentile_filter()
gaussian_filter() with a sigma parameter
"""

#example median filtering, filter of size 9 (9x9)
median_filtered = ndi.median_filter(im, size=9)
plt.imshow(median_filtered, cmap='gray')
plt.title('Median Filtered Image')
plt.show()
