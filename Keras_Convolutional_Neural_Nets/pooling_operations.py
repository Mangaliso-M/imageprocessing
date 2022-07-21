#@author: Mangaliso M. Mngomezulu
#Pooling -  an idea of reducing the network parameters

#max pooling = choose a region, replace it with its max pixel in the next window

#assume im in the input image
im = np.array([7,8])

result=np.zeros(im.shape[0]//2, im.shape[1]//2) #it has half the size as the original image

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        result[i,j] = np.max(im[i*2 : i*2+2, j*2:j*2+2])


#MaxPool2D object can be used  to allow for this operation on the image inputs
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPool2D

model = Sequential()

model.add(Conv2D(5, kernel_size=3, activation='relu', input_shape=(img_rows, img_cols, 1)))

model.add(MaxPool2D(2)) #window of size 2 x 2, where the max is taken

model.add(Conv2D(15, kernel_size=3, activation='relu', input_shape=(img_rows, img_cols, 1)))

model.add(MaxPool2D(2))

model.add(Flatten())

model.add(Dense(3, activation='softmax'))

#the pooling operation dramatically reduces the number of parameters