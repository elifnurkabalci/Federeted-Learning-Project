import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np


def learning(x_train, y_cat_train, x_test, y_cat_test):
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(4, 4), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    # output layer
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_cross entropy', optimizer='adam', metrics=['accuracy'])

    early_stop = EarlyStopping(monitor='val_loss', patience=1)
    model.fit(x_train, y_cat_train, epochs=10, validation_data=(x_test, y_cat_test), callbacks=[early_stop])

    model.save("model.h5")
    return model


def learning_metrics(model, x_test, y_cat_test, y_test):
    metrics = pd.DataFrame(model.history.history)
    # metrics
    metrics.plot()
    metrics[['loss', 'val_loss']].plot()
    metrics[['accuracy', 'val_accuracy']].plot()
    model.evaluate(x_test, y_cat_test, verbose=0)
    prediction_x = model.predict(x_test)
    predictions = np.argmax(prediction_x, axis=1)
    print(classification_report(y_test, predictions))
    confusion_matrix(y_test, predictions)
