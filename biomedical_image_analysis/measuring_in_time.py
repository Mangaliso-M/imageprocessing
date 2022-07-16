#@author: Mangaliso Moses Mngomezulu
#how to measure the ejection fraction of a person's heart

import numpy as np
import scipy.ndimage as ndi

"""
 ejection_fraction = ( LVmax - LVmin ) / LVmax #ventricle when relaxed - when squeezed / when reladed

 Procedure
 1. segment the left ventricle
 2. For each 3d volume in the time series, calculate the volume
 3. From the Volumes, find the max and the min
 4. Calculate the ejection fraction

 the data is stored in this format:
 (t, z, x, y)  where t is the time
"""

#calculate the voxel volume in mm^3
vol= {} #temp val
vol.meta = [1,2,3,4] #temp val
d0,d1,d2,d3 = vol.meta['sampling'] #vol is to be made up from dicom images

dxovel = d1 * d2 * d3

#Instantiate an empty list
ts = np.zeros(20)

for t in range(20):
    nvoxels = ndi.sum(1, labels[t],index=1)
    ts[t] = nvoxels * dxovel

plt.plot(ts)
plt.show()
# a graph of the time series and volmetric changes of the ventricle is shown the min and max volume are extacted from there and then the ejection fraction is computed


#ts is the time series numpy array

min_vol = ts.min()
max_vol = ts.max()

ejec_fract = (max_vol - min_vol) / max_vol #an estimate of the ejection fraction





