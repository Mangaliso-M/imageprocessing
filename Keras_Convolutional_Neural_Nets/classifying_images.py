#@author: Mangaliso M. Mngomezulu
#description: image classification basic step

#one hot encoding of the classes is generated relative to how the classes appear in the dataset

#assume the classes appear in this order in the dataset
from unicodedata import category
import numpy as np

labels = ["shoe","dress","shoe","t-shirt","shoe","t-shirt","shoe","dress"]

#generate the one-hot encoding vector for this one.
#each row has a dimension that is the same as the number of classes, the class which is true for that object is labelled with a 1 and all else are 0s.

categories = np.array(["t-shirt","dress","shoe"])
n_catergories = 3
one_hot_vec = np.zeros((len(labels), n_catergories)) #3x8

for i in range(len(labels)):
    j = np.where(categories == labels[i])
    one_hot_vec[i,j] = 1

print(one_hot_vec)


