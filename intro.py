
#Author: Mangaliso M Mngomezulu
#desc: Datacamp image processing course

from skimage import data
from skimage import color
import matplotlib.pyplot as plt

#load rocket image, found in the library
rocket_image = data.rocket()


#the show image function
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

#display the image of a rocket
show_image(rocket_image,"Rocket Image")

#show the gray scale version of the rocket image
show_image(color.rgb2gray(rocket_image), "gray rocket image")

#covert the gray scale image of the rockect to the original color, and display
rgb_rocket = color.rgb2gray(rocket_image)

#convert a color image to a grayscale image
color_rocket = color.gray2rgb(rgb_rocket)

#now display the recoverted image, since color is not preserved in the conversion, the new color image is in fact black and white
show_image(color_rocket) 

print("Lesson 1, done. ")
print("The branch with lessons from the datacamp are on the fromlesson branch")