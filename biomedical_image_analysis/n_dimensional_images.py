#@Author: Mangaliso M. Mngomezulu
#description: multilayer images (3D, 4D, ... ND), images can be represented in volumentric space, stacked on top of each other
#paths specified assume that the source file is used within its repository.

import imageio 
import numpy as np
import os 


image1 = imageio.imread('./datasets/tcia-chest-ct-sample/chest-220.dcm')
image2 = imageio.imread('./datasets/tcia-chest-ct-sample/chest-221.dcm')
image3 = imageio.imread('./datasets/tcia-chest-ct-sample/chest-222.dcm')

print("The shape for image 2 is: ",image2.shape) #(512, 512)

volmetric_image = np.stack([image1, image2, image3]) 


#read the directory as one volmetric data for processing,uses metadata to sort the list, if metadata is not available it defaults to ...
vol = imageio.volread('./datasets/tcia-chest-ct-sample/')

if __name__ == "_main_":
    #(3, 512, 512)
    print("The shape for the volmetric image data is:", volmetric_image.shape)

    #imageio.volread() reads data as a volume directly from disk, takes as an arg the folder name
    print("directory files: ",os.listdir('./datasets/tcia-chest-ct-sample/'))

#the metadata from the volume can be unpacked 
#im1, im2, im3 = vol.meta['attribute']
