#@Author: Mangaliso M. Mngomezulu
# read world applications for image processing in python

"""
A combination of the module's covered work.

1. convert images to grayscale before detecting edges/corners
2. reducing noise and restoring images
3. blurring faces detected
4. Approximation of object sizes

for the case below, find all the faces in the picuture and blur them
"""
from skimage.feature import Cascade #used to detect the faces
from skimage.filters import gaussian #used to blurr the faces
from skimage import data
import skimage.io as skimio
from custom_lib import getFace, mergeBlurryFace, show_image

#load the trained model/file from the module
trained_file = data.lbp_frontal_face_cascade_filename()

#initialize a detector
detector  = Cascade(trained_file) #this is an object of the Cascase class

#load the image with the students
students_img =  skimio.imread("images/students.jpg")

detected_face_box_coords = detector.detect_multi_scale(img=students_img,
                                              scale_factor=1.2, #this is used to multiply the searching window for each step of the search
                                              step_ratio=1, #exhaustive search for value 1, higer values will be faster but poor
                                              min_size=(10,10), #smallest window size
                                              max_size=(200,200) #largest window size
                                              )

#on each detected face, obtain the face cropped from the detected coordinates
for face in detected_face_box_coords:
    face = getFace(face, students_img) #crop the face out of the image
    gaussian_face = gaussian(face, sigma=10)

    #merge the blurry face back to the image
    resulting_image = mergeBlurryFace(students_img, gaussian_face, face)
    
show_image(resulting_image,"Blurred faces")
