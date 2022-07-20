#@author: Mangaliso M. Mngomezulu
#description: Introduction to CNNs

#import keras
from dataclasses import dataclass
import imageio
import matplotlib.pyplot as plt

im = imageio.imread('./datasets/stop_sign.jpg')

#index a location in the array
print(im[500,500]) #at location 500, 500 there is a (r,g,b) arr

#set all the green and blue values of the image to 0
im[:,:,1] = 0 #first 2 are for the x,y, then 1 is for the green, then 2 for blue
im[:,:,2] = 0 #blue part

#or set the image to have no read, no blue but full intensity on the green channel
im[200:400, 300:500, :] = [0,1,0] #x is vertical, y is horizontal

plt.imshow(im)
plt.title('Stop Sign')
plt.show()

data = im

# Set the red channel in this part of the image to 1
data[:10,:10,0] = 1 

# Set the green channel in this part of the image to 0
data[:10,:10,1] = 0

# Set the blue channel in this part of the image to 0
data[:10,:10,2] = 0

# Visualize the result
plt.imshow(data)