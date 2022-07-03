#@Author: Mangaliso M. Mngomezulu
#description: Introduction to biomedical imaging

#read an image

import imageio #it can also read .dcm files, which is the common format for medical images

#the data used was locally refrenced
im = imageio.imread('../datasets/tcia-chest-ct-sample/chest-220.dcm')

