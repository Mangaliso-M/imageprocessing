import matplotlib.pyplot as plt
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


def show_image_with_detected_corners(image, coords, title="Corners detected"):
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:,1], coords[:, 0], '+r', markersize=15)
    plt.axis('off')
    plt.show()