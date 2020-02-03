import numpy as np
from neural_network import build_model
from balance_data import balance_data
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from global_var import *

data = np.load(DATA_DIR, allow_pickle=True)

X = np.array([data[i][0] for i in range(len(data))])
y = np.array([data[i][1] for i in range(len(data))])

X = X.reshape([-1, FINAL_HEIGHT, FINAL_WIDTH, 1])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = build_model(FINAL_HEIGHT, FINAL_WIDTH)
model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=[x_test, y_test])

model.save('my_model.h5')
