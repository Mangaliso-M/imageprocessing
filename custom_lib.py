from matplotlib import patches
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

def show_detected_face(result, detected_face_coords, title="Face image"):
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap('gray')
    plt.title(title)
    #plt.axis('off')
    
    for patch in detected_face_coords: #more than one face could be detected
        img_desc.add_patch(
            patches.Rectangle(
                (patch['c'], patch['r']),
                patch['width'],
                patch['height'],
                fill=False, color='r', linewidth=1
            )
        )
    plt.show()

def getFace(d, image): #d is the detected face's coords, from image
    ''' Extracts the face rectangle from the image using the coordinates of the detected.
    '''
    x,y = d['r'], d['c'] #top left corner of the detected rectangle,
    width, height = d['r']+d['width'], d['c']+d['height']

    #extract the detected face
    face = image[x:width, y:height]
    return face


def mergeBlurryFace(original, gaussian_image, d):
    ''' merge the blurry face back to the image
    '''
    x,y = d['r'], d['c'] #top left corner of the detected rectangle,
    width, height = d['r']+d['width'], d['c']+d['height']
    
    original[x:width, y:height] = gaussian_image
    return original