import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

x_train = np.random.uniform(-100, 100, (500, 2)) 
y_train = np.array([a + b for a, b in x_train])

model = keras.Sequential()

model.add(Dense(units=1, input_shape=(2,), activation='linear'))

model.compile(loss='mean_squared_error', 
              optimizer=keras.optimizers.Adam(0.1))

print("Начало обучения...")
history = model.fit(x_train, y_train, epochs=500, verbose=False)
print("Обучение завершено.")

test_data = np.array([[15.5, 24.5]])
prediction = model.predict(test_data)
print(f"Результат для 15.5 + 24.5: {prediction[0][0]}")
print(f"Ожидаемый результат: 40.0")

weights = model.get_weights()
print(f"Веса (должны быть ~1.0): {weights[0].flatten()}")
print(f"Смещение (bias, должно быть ~0.0): {weights[1]}")

plt.plot(history.history['loss'])
plt.grid(True)
plt.show()