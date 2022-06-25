#@Author: Mangaliso Mngomezulu
#how to flip images vertically and horizontally (image matrix rotation)

from skimage import data, io
import numpy as np
import matplotlib.pyplot as plt

#load the image from the skimage library
cat = data.cat()

#flip horizontally
cat_horizontal_flip = np.fliplr(cat)

#flip the image vertically
cat_vertical_flip = np.flipud(cat)

#original image
io.imshow(cat)
plt.title("Original Cat image")
plt.show()

#display the flipped images
io.imshow(cat_vertical_flip)
plt.title("Vertically flipped image")
plt.show()

io.imshow(cat_horizontal_flip)
plt.title("Horizontally flipped image")
plt.show()