#Author: Mangaliso Mngomezulu
#get the shape of an image's data (The shape of the matrix)
import skimage
import numpy 
import matplotlib.pyplot as plt

#the show image function
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

#load predefined images from skimage
chelsea_image = skimage.data.cat()  #color image
cell_image = skimage.data.cell() # cell image

#get the shape of the matrix
print("colored chelesea image shape:", numpy.shape(chelsea_image))

#get the shape of the grayscale image
print("Grayscale coins image shape:", numpy.shape(cell_image))

#display the images for confirmation
show_image(chelsea_image, "Chelsea the cat")
show_image(cell_image, "Cell image")