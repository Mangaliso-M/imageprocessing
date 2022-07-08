#@author: Mangaliso M. Mngomezulu 
#description: Image intensities

import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

im = imageio.imread('./datasets/sunnybrook-cardiac-mr/SCD2001_000/SCD2001_MR_209.dcm')

#pixels are 2d picture elements
#voxels are 3d picture elements
#im.size gives the size of the image

#histogram
hist=ndi.histogram(im, min=0, max=255, bins=256)
plt.plot(hist)
plt.show()

#skewed distributions can be equalized through histogram equalization
cdf = hist.cumsum() / hist.sum() #cumulative distribution function

#apply the cdf to the image, the rescale by 255
im_equalized = cdf[im] * 255

plt.imshow(im_equalized)
plt.title("Equalized Image")
plt.show()

#the histogram of the equalized image can be computed similary.


#the two images can be displayed using the techniques for advanced plotting
fig,axes = plt.subplots(2,1)
axes[0].imshow(im)
axes[1].imshow(im_equalized)
plt.show()
