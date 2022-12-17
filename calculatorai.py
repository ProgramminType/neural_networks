import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.activations import relu
from tensorflow.keras import regularizers

inputaddition = np.array(
    [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1]])

outputsum = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]])

model = keras.Sequential([
    keras.layers.Dense(6, input_shape=(2,), activation='relu',
                       kernel_regularizer=regularizers.l1(0.01)),
    #                                                     0.01 is the reg rate
    keras.layers.Dense(8, input_shape=(2,), activation='relu',
                       kernel_regularizer=regularizers.l1(0.01)),
    #                                                     0.01 is the reg rate
    keras.layers.Dense(1, input_shape=(2,), activation='relu',
                       kernel_regularizer=regularizers.l1(0.01))
    #                                                     0.01 is the reg rate
])

model.compile(optimizer='sgd', loss='mse')

network = model.fit(inputaddition, outputsum, epochs=5000)

loss_start = network.history['loss'][0]
loss_finish = network.history['loss'][4999]
subtracted = loss_start - loss_finish
increase = subtracted / loss_start
percent = increase * 100
percent = round(percent, 2)
print("Loss Change: " + str(percent) + "%")

try:
    while True:
        number1 = input("What is the first number you would like to add? ")
        number2 = input("What is the second number you would like to add? ")
        number1 = str(number1)
        number2 = str(number2)
        check = input("Is this your final equation? " + number1 + " + " + number2 + " = ")
        if check == "y":
            number1 = float(number1)
            number2 = float(number2)
            inputadditiontest = np.array([[number1, number2]])
            predictions = model.predict(inputadditiontest)
            predictions = float(predictions)
            predictions = round(predictions, 0)
            print(predictions)

        else:
            number1 = input("What is the first number you would like to add? ")
            number2 = input("What is the second number you would like to add? ")
            number1 = str(number1)
            number2 = str(number2)
            check = input("Is this your final equation? " + number1 + " + " + number2 + " = ")
            if check == "y":
                number1 = float(number1)
                number2 = float(number2)
                inputadditiontest = np.array([[number1, number2]])
                predictions = model.predict(inputadditiontest)
                predictions = float(predictions)
                predictions = round(predictions, 0)
                print(predictions)
except KeyboardInterrupt:
    pass
