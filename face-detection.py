#Author: Mangaliso M. Mngomezulu
#facial detection

from skimage.feature import Cascade
from skimage import data
from custom_lib import show_detected_face

#load the trained model/file from the module
trained_file = data.lbp_frontal_face_cascade_filename()

#initialize a detector
detector  = Cascade(trained_file) #this is an object of the Cascase class

#load the astronaut image
astronaut_img = data.astronaut() #this will return the co-ordinates of the box that contains the face.

detected_face_box_coords = detector.detect_multi_scale(img=astronaut_img,
                                              scale_factor=1.2, #this is used to multiply the searching window for each step of the search
                                              step_ratio=1, #exhaustive search for value 1, higer values will be faster but poor
                                              min_size=(10,10), #smallest window size
                                              max_size=(200,200) #largest window size
                                              )

print("Face detected at: ", detected_face_box_coords)

#show the detected face 
show_detected_face(astronaut_img, detected_face_box_coords)