# -*- coding: utf-8 -*-
"""SVM_Train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oDPWWFFa87ZePOCYWwr_v5QaIu0hLT0s
"""

from google.colab import drive
drive.mount('/content/drive/')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import  svm, metrics
from sklearn.metrics import accuracy_score
import random

from google.colab import drive
drive.mount('/content/drive')

!ls "/content/drive/My Drive"

alarm_arr=np.load('/content/drive/My Drive/alarm.npy')
bed_arr=np.load('/content/drive/My Drive/bed.npy')
beard_arr=np.load('/content/drive/My Drive/beard.npy')
banana_arr=np.load('/content/drive/My Drive/banana.npy')
train_size=25000
train_len=100000
test_size=1000
test_len=4000
label_size=4
ls1=[]
for x in range(5000):
    ls1.append(random.randint(0,100000))
tr=[]
for i in range(4):
    for j in ls1:
        if(i==0):
            tr.append(alarm_arr[j])
        elif(i==1):
            tr.append(bed_arr[j])
        elif(i==2):
            tr.append(beard_arr[j])
        else:
            tr.append(banana_arr[j])
train=np.array(tr)
train=train/255.0
from keras.utils import np_utils
data_y = np.zeros((20000,))
data_y[5000:10000]=1
data_y[10000:15000]=2
data_y[15000:]=3
data_y = np.array(data_y)
train, test, data_y, y_test = train_test_split(train,data_y, test_size=0.3, random_state=13)
classifier = svm.SVC(gamma=0.001)
classifier.fit(train,data_y)
y_pred = classifier.predict(test)
print("Classification report for classifier %s:\n%s\n"% (classifier, metrics.classification_report(y_test, y_pred)))
print(accuracy_score(y_test, y_pred))
