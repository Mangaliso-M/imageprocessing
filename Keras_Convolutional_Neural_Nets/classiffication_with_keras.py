#@author: Mangaliso M. Mngomezulu
#description: Classification with Keras

from keras.model import Sequential#a general model

from keras.layers import Dense #in a Dense network,all nodes from previous layer are connected to all layers in the next layer
#the first layer in the network is connected to all the pixels from the image
#the assumption is that there is some image data that is available for use  in the model training

model = Sequential()
#train_data.shape gives (number of samples, input_img_width, input_img_height, 1 (for black and white images))
model.add(Dense(10, activation='relu', input_shape=(784,))) #first layer: the 10 is for the nodes. is for  input shape is for the numper of inputs each node should expect
model.add(Dense(10, activation='relu')) #second layer: 10 nodes
model.add(Dense(3, activation='softmax')) #output later

#at this step the model has been set up, then the next step is to compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#the model expect the images to be rows in an array, so reshape the data to fit well
train_data = train_data.reshape((50, 784)

#train the model
#at the end of every epoch of training, the model is validated on the training set.
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)

#finally, the testing/ the assumption is that the test data was defined somewhere
test_data = test_data.reshape((10,784))
model.evaluate(test_data, test_labels)