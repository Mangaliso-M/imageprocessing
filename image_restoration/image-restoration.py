#@Author: Mangaliso M. Mngomezulu
#description: image restoration

from skimage.restoration import inpaint
from skimage import data
from custom_lib import plot_comparison, get_mask

faulty_image = data.astronaut() #put a defect image here    

#get the mask
mask  = get_mask(faulty_image)

#apply the mask to the image to compute the restored image
restored_image = inpaint.inpaint_biharmonic(faulty_image, mask, multichannel=True) #multichannel = true for colored images

plot_comparison(faulty_image, restored_image, "Restored Image")