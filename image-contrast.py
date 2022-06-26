#@Author: Mangaliso M. Mngomezulu
#constrast enhancement - the spread of the histogram of the image (the diffrence between the min and max pixel in the image)

from skimage import exposure, data
import matplotlib.pyplot as plt 

def plot_comparison(original, filtered, title_filtered):
    
    fig, (img1,img2) = plt.subplots(ncols=2, figsize=(8,6), sharex=True, sharey=True)
    
    img1.imshow(original, cmap=plt.cm.gray)
    img1.set_title('Original image')
    img1.axis('off')

    img2.imshow(filtered, cmap=plt.cm.gray)
    img2.set_title(title_filtered)
    img2.axis('off')

def equalized_img():
    #equalized image
    image  = data.astronaut()
    eqaulized_image = exposure.equalize_hist(image)
    plot_comparison(image, eqaulized_image, "Equalized Image")
    plt.show()

equalized_img()


#adaptive equalization
def adaptive_equalization():
    image = data.astronaut()
    image_adaptive = exposure.equalize_adapthist(image, clip_limit=0.05)
    plot_comparison(image, image_adaptive, "Adaptive Equalization")
    plt.show()

adaptive_equalization()