# -*- coding: utf-8 -*-
"""CNN_Train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15wbGVQIfBzVC9APnYBjRd46GdeljsgzA
"""

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, Flatten, MaxPooling2D, Dropout, Conv2D
from keras.utils import np_utils
from keras.layers.normalization import BatchNormalization
import os
import cv2
from keras.layers.advanced_activations import LeakyReLU

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

!gsutil -m cp gs://quickdraw_dataset/full/numpy_bitmap/* ./data

!ls ./data

alarm = np.load('./data/alarm clock.npy')
book = np.load('./data/book.npy')
campfire = np.load('./data/campfire.npy')
cloud = np.load('./data/cloud.npy')

data_x = []
for i in range(0,10000):
    a1=alarm[i].reshape(28,28)
    data_x.append(a1)
for i in range(0,10000):
    a1=book[i].reshape(28,28)
    data_x.append(a1)
for i in range(0,10000):
    a1=campfire[i].reshape(28,28)
    data_x.append(a1)
for i in range(0,10000):
    a1=cloud[i].reshape(28,28)
    data_x.append(a1)

plt.imshow(alarm[0].reshape(28,28), interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(book[0].reshape(28,28), interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(campfire[0].reshape(28,28), interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(cloud[0].reshape(28,28), interpolation='nearest',cmap='gray')
plt.show()

data_x = np.array(data_x)

print data_x.shape

data_x = data_x.reshape(-1,28,28,1)
data_x = data_x/255.0

data_y = np.zeros((40000,))

data_y[:10000] = 0
data_y[10000:20000] = 1
data_y[20000:30000] = 2
data_y[30000:] = 3

data_y = np_utils.to_categorical(data_y)

print data_y

batch_size = 64
epochs = 30
num_classes = 4

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28,28,1),padding='same'))
model.add(LeakyReLU(alpha=0.05))
model.add(MaxPooling2D((2, 2),padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu',padding='same'))
model.add(LeakyReLU(alpha=0.05))
model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu',padding='same'))
model.add(LeakyReLU(alpha=0.05))                  
model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(LeakyReLU(alpha=0.1))                  
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(data_x, data_y, batch_size=batch_size,epochs=epochs,validation_split=0.10)

from google.colab import drive
drive.mount('/content/drive')

model.save('/content/drive/My Drive/Quick_Draw_CNN.h5')

