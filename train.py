import numpy as np
import pandas as pd



from keras.layers import Dense, Convolution2D
from keras.models import Sequential
from keras.layers.advanced_activations import PReLU
from utils import load_data



data = load_data()

labels = pd.read_csv('stage1_labels.csv/stage1_labels.csv')

num_examples = data.shape[0]

data = np.reshape(data,[num_examples,512,512,1])


print data.shape

print labels.shape

print

#model = Sequential()

#model.add(Convolution2D(80,57,6,input_shape=(512,512,1),activation=PReLU(init='zero')))
#model.add(Dense(10,activation='relu'))

#model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

#model.fit(data,labels,batch_size = 10, nb_epoch=100,verbose=1,shuffle=True)

#scores = model.evaluate(data,labels,batch_size=10)

#print scores[0]

#print scores[1]