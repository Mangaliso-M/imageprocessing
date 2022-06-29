#@Author: Mangaliso M. Mngomezulu
#description: edge detection

#Canny edge detection (high efficiency and low execution time)
#import matplotlib.pyplot as plt
from skimage.feature import canny
from skimage import data, color
from custom_lib import plot_comparison, show_image

coins = data.coins()
#coins = color.rgb2gray(coins), already rgb
canny_edges = canny(coins)

show_image(canny_edges,"Canny Edge Detection (sigma = 1 by default?)")


#apply the canny edge detector with varying values, the sigma attribute in the canny edge detector makes it a Gaussian Edge Detector
#higher sigma values remove more noise
canny_edges_0_6 = canny(coins, sigma=0.6)

show_image(canny_edges, "Sigma=0.6")
