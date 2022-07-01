#@Author: Mangaliso M. Mngomezulu
#description: Introduction to biomedical imaging

#read an image

import imageio #it can also read .dcm files, which is the common format for medical images

im = imageio.imread('body-001.dcm')
