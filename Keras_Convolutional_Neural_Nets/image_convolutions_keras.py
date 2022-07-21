#@author: Image convolutions in keras


from pickletools import optimize
from keras.layers import Conv2D, Dense, Flatten
from keras.model import Sequential

#instead of every layer connected directly to each layer, they are connected through a convolution
#10 units and kernels of size 3 makes 90 parameters for this layer
#Conv2D(10, kernel_size=3, activation='relu') #10 convolution units, the kernel of the convolution is adjusted by back propagation


model = Sequential()

model.add(Conv2D(10, kernel_size=3, activation='relu', input_shape=(img_rows, img_cols, 1)))

#Flattern serves as a connection between Convolution and Densely connected layers
model.add(Flatten()) #takes the output of the convolution,flatterns it into a 1 dimensional array then makes it ready for the next layer to absorb
#in this case the output is one of 3 classes of clothing, 3 units are then used to handle that
model.add(Dense(3, activation='softmax'))
#now that the model architecture is complete, compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train_data.shape #gives (50, 28, 28, 1) which means its 50 samples of clothing images, each size 28 by 28, the 1 is for grayscale images


#sometimes we may want to reshape the array, but in this case just train
#training
#a batch size parameter can be defined which gives a number of images to be used
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)

#test the model on unseen data
model.evaluate(test_data, test_labels, epochs=3)
