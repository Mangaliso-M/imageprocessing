#@Author: Mangaliso M. Mngomezulu
#Going deeper with understanding CNNs

#previous nets had one layer, now we make a deep CNN

model = Sequential()

#first layer
model.add(Conv2D(10, kernel_size=2, activation='relu', input_shape=(img_rows, img_cols, 1)), padding='equal')


#second layer
model.add(Conv2D(10, kernel_size=2, activation='relu'))

model.add(Flatten())

model.add(Dense(3, activation='softmax'))

#for multiple layers,  much ahead layers detect complex objects based on simple features found earlier in the network
