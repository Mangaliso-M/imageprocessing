#Author: Mangaliso M Mngomezulu
#description: image thresholding
#to see the effects, call the functions defined here, functions defined below are custom but they use the built in functions
#for some images, first convert to grayscale before doing any thresholding

from tabnanny import verbose
#from cv2 import threshold
from numpy import binary_repr
from skimage import data, io
from skimage import color
from skimage.filters import try_all_threshold , threshold_otsu, threshold_local #..otsu if for optimal thresholding
import matplotlib.pyplot as plt

#obtain the optimal threshold value
thresh = 127 # (255-1) / 2
#load the image from skimage
image = data.page()

def display_thresholded_img():
    #use the thresh value to compare against the original image's values
    binary_image = image > thresh
    io.imshow(binary_image)
    plt.title("Thresholded page image")
    plt.show()
#display_thresholded_img()

def try_all_custom():
    #it is possible to try out all the thresholding algorithms from skimage, by the used of a predefined procedure
    #one can then choose the best algorithm here
    image = data.page()
    fig, ax = try_all_threshold(image, figsize=(12, 10), verbose=True)
    plt.show()
#try_all_custom()

#for images with an even background
def find_optimal_global_threshold():
    image = data.camera()
    thresh = threshold_otsu(image)
    binary_global_threshold = image > thresh
    io.imshow(binary_global_threshold)
    plt.title("Binary globally thresholded image")
    plt.show()
#find_optimal_global_threshold()

def localthreshold():
    image = data.camera()
    region_size = 35 #the size of the regions to apply the thresholding in
    locally_threshold_value  = threshold_local(image, region_size, offset=10)
    binary_locally_thresholded_img = image > locally_threshold_value
    io.imshow(binary_locally_thresholded_img)
    plt.title("Locally Thresholded image")
    plt.show()

localthreshold()


