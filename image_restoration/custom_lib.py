import matplotlib.pyplot as plt
import numpy as np

def plot_comparison(original, filtered, title_filtered):
    
    fig, (img1,img2) = plt.subplots(ncols=2, figsize=(8,6), sharex=True, sharey=True)
    
    img1.imshow(original, cmap=plt.cm.gray)
    img1.set_title('Original image')
    img1.axis('off')
   
    img2.imshow(filtered, cmap=plt.cm.gray)
    img2.set_title(title_filtered)
    img2.axis('off')
    plt.show()

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def get_mask(image):
    '''Creates a mask with three defect regions, copy the image dimensions, and set specific indexes to have 1s while the rest have 0s'''
    mask = np.zeros(image.shape[:-1]) #use the shape of the image to intialize this matrix

    #these define the faulty region(s) of the image, in the form mask[x_1:y_1, x_2:y_2]
    mask[101:106, 0:240] = 1
    mask[152:154, 0:60] = 1
    mask[153:155, 60:100] = 1
    mask[154:156, 100:120] = 1
    mask[155:156, 120:140] = 1

    mask[212:217, 0:150] = 1
    mask[217:222, 150:256] = 1 
    
    return mask