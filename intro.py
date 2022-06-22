
#Author: Mangaliso M Mngomezulu
#desc: Datacamp image processing course

from skimage import data
from skimage import color
import matplotlib.pyplot as plt

#load rocket image, found in the library
rocket_image = data.rocket()

#covert the image to grayscale
#grayscale = color.rgb2gray(original)

#convert grayscale to rgb
#rgb = color.gray2rgb(grayscale)

#the show image function
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

#display the image of a rocket
show_image(rocket_image,"Rocket Image")