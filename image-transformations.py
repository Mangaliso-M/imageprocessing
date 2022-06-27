#@Author: Mangaliso M. Mngomezulu
#image transformation

from matplotlib import widgets
from skimage.transform import rotate, rescale, resize
from skimage import data, io
from custom_lib import plot_comparison, show_image

#rotate an image 90' clockwise
image  = data.astronaut()
rotated_img = rotate(image, -90)
plot_comparison(image, rotated_img, "Rotated image")

#resizing the image
height = 200
width = 200
resized_image = resize(image,(height, width), anti_aliasing=True) #aliasing makes the image looks bad
show_image(resized_image, "resized image")
show_image(image,"Original Image")

#propotional resizing
height = image.shape[0]/4
width = image.shape[1]/4
resized_image = resize(image, (height, width), anti_aliasing=True)
plot_comparison(image, resized_image, "Resized Image")

#rescaling the image, for image enlargement!
rescaled_image = rescale(image, 0.5, anti_aliasing=True, multichannel=True) #aliasing makes the image looks bad
plot_comparison(image, rescaled_image, "Rescaled image")