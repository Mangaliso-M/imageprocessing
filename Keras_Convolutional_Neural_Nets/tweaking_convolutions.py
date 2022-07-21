#@author: Mangaliso M. Mngomezulu
#tweaking convolutions

#Zero padding the input image helps with making sure that the image output can be of the same size as the input image

#padding='valid' means no padding will be done on the imput images
model.add(Conv2D(10, kernel_size=3, activation='relu',
         input_shape=(img_rows, img_cols, 1)), padding='valid')


#padding='same' means that the input to the current layer will be such that the output has the same dimensions as the input layer
model.add(Conv2D(10, kernel_size=3, activation='relu',
         input_shape=(img_rows, img_cols, 1)), padding='same')


#the stride is the size of the steps taken when processing the input kernel, it also affects the output size
#the stride and padding can be used together but its not always a good idea
model.add(Conv2D(10, kernel_size=3, activation='relu',
         input_shape=(img_rows, img_cols, 1)), stride=2)

#the kernel can be used to aggregate data from wide spread pixels, the dilation rate parameter is used to allow the kernel entries to be dilated while acting on the data
model.add(Conv2D(10, kernel_size=3, activation='relu',
         input_shape=(img_rows, img_cols, 1)), dilation_rate=2)



