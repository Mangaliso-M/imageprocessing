#@author: Mangaliso M Mngomezulu
#descript: advanced image plotting, plotting many at once

import imageio
from n_dimensional_images import vol #from a custom file
import matplotlib.pyplot as plt

volumetric_data = vol

fig, axes = plt.subplots(nrows=1, ncols=3) # a display with 3 columns to show images, in one row

#display the three slices on the figure's axis
axes[0].imshow(volumetric_data[0], cmap='gray')
axes[1].imshow(volumetric_data[1], cmap='gray')
axes[2].imshow(volumetric_data[2], cmap='gray')

#remove the axis for each of the three axes
for ax in axes: 
    ax.axis('off')

#now display the figure
plt.show()


#alternatives for slicing volmetric data into 2d images for display
view_a = vol[0, :, :] #one image (2nd vs 3rd)
view_b = vol[ :0, :] #one image (1st vs 3rd)
view_c = vol[ :, :0] #one image (1st vs 2nd)
#view_a = vol[0] #one image

#print(view_a.shape)
#plt.imshow(view_a)
#plt.show()

#modifying the aspect ratio
#it happens that the images donot have the same dimensions, yet we want to stack them. So the procedure is to stretch the pixels on one side so that the images can be compatible fo