

#example of a dense 2 layer network

model = Sequential()

model.add(Dense(10, activation='relu', input_shape=(784,)))

model.add(Dense(10, activation='relu'))

model.add(Dense(3, activation='softmax'))


"""
Computing the numper of parameters goes as follows:

#assume the images are 28x28 pixels = 784 for input shape

Layer 1: 10 units, each connected to all the input pixels: 

Layer 2: 10 units, each connected  all the 10 previous ones:

Layer 3: 3 units, each connected to the previous 10

Example model.summary() output

Layer(type)                Output shape               Param#
===========================================================
dense_1(Dense)           (None, 10)                   7850 = 784x10+ 10 biases
-----------------------------------------------------------
dense_2(Dense)           (None, 10)                   110 = 10 x 10 + 10 biases
-----------------------------------------------------------
dense_3(Dense)           (None, 3)                    33 = 3 x 10 + 10 biases
===========================================================
Total params: 7,993
Trainable params: 7,993
Non-trainable params: 0
-----------------------------------------------------------

"""

#once we introduce kernels, ingore the input size, the kernel decides the result
