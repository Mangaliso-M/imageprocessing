#@Author: Mangaliso M. Mngomezulu
#description: Introduction to biomedical imaging

#read an image

import imageio #it can also read .dcm files, which is the common format for medical images
import matplotlib.pyplot as plt

#the data used was locally refrenced
im = imageio.imread('./datasets/tcia-chest-ct-sample/chest-222.dcm')

#print(type(im))
#print(im)
#print(im.meta.keys()) #get the image metadata keys, they can be used to acces the values of the metadata
#print(im.meta['StudyTime']) #example of reading  a value from the metadata

#plotting images
plt.imshow(im, cmap='gray', vmin=-100, vmax=100) #vmin and vmax attributes are optional and they help increase the contrast by setting the min and max values
plt.axis('off')
plt.show()