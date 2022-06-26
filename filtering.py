#@Author: Mangaliso Mngomezulu
#Filtering, skimage library
from skimage.filters import sobel, gaussian
from skimage import data, color
import matplotlib.pyplot as plt

#sobel edge detection
image = data.camera()

def plot_comparison(original, filtered, title_filtered):
    
    fig, (img1,img2) = plt.subplots(ncols=2, figsize=(8,6), sharex=True, sharey=True)
    
    img1.imshow(original, cmap=plt.cm.gray)
    img1.set_title('Original image')
    img1.axis('off')

    img2.imshow(filtered, cmap=plt.cm.gray)
    img2.set_title(title_filtered)
    img2.axis('off')

def apply_sobel():
    edge_sobel = sobel(image) #the function requires a 2d image in gray scale.
    plot_comparison(image, edge_sobel, "Sobel Filtered version")
    plt.show()
#apply_sobel()

def gaussian_smoothing():
    image = data.rocket()
    image = color.rgb2gray(image)
    filtered_kidney_image = gaussian(image)
    plot_comparison(image, filtered_kidney_image, "Gaussian Filtered Image")
    plt.show()

gaussian_smoothing()