import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model = Sequential([ 
  Conv2D(16, (3,3), activation= 'relu', input_shape= (300,300,3)),
  MaxPooling2D(2,2),
  Conv2D(32, (3,3), activation= 'relu'),
  MaxPooling2D(2,2),
  Conv2D(64, (3,3), activation= 'relu'),
  MaxPooling2D(2,2),
  Conv2D(64, (3,3), activation= 'relu'),
  MaxPooling2D(2,2),
  Conv2D(64, (3,3), activation= 'relu'),
  MaxPooling2D(2,2),
  Flatten(),
  Dense(512, activation = 'relu'),
  # For binary classification I use 1 noran in output layer
  # I use sigmoid activation function because I vat to get result between 0-1
  Dense(1, activation= "sigmoid")
  ])


# See summary of the model
model.summary()


# Compile model
from tensorflow.keras.optimizers import RMSprop

model.compile(optimizer = RMSprop(learning_rate = 0.001),
              loss = "binary_crossentropy",
              metrics = ["accuracy"])


              
