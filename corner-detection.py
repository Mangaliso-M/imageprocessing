#@author: Mangaliso M. Mngomezulu
#detection of corners in an image (a corner is a junction of contours)

#harris corner detection
from skimage.feature import corner_harris, corner_peaks
from skimage import data
from custom_lib import show_image, show_image_with_detected_corners
#requires grayscale images

image = data.checkerboard()

#corner detection using the harris corner detector
harris_measure  = corner_harris(image)

show_image(harris_measure, "Potential corners")

#get the co-ordinates of the corners in the image
coords = corner_peaks(corner_harris(image), min_distance=6, threshold_rel=0.02) #min distance between the corners 

#print the count of the corners co-ordinates
print(len(coords)," corners were found in the image")

show_image_with_detected_corners(image, coords)