import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

max_words = 10000   
max_len = 200

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_words)

x_train = sequence.pad_sequences(x_train, maxlen=max_len, padding='pre')
x_test  = sequence.pad_sequences(x_test,  maxlen=max_len, padding='pre')

print(f"Форма обучающей выборки: {x_train.shape}")
print(f"Форма тестовой выборки:  {x_test.shape}")
print(f"Баланс классов в train: {np.bincount(y_train)}")

model = Sequential()
model.add(Embedding(max_words, 128, input_length=max_len))
model.add(LSTM(64, activation='tanh', dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.001),
    metrics=['accuracy']
)

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=2,
    restore_best_weights=True
)

history = model.fit(
    x_train, y_train,
    batch_size=64,
    epochs=5,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

scores = model.evaluate(x_test, y_test, verbose=0)
print(f"\nТочность на тестовой выборке: {scores[1]*100:.2f}%")
print(f"Потери на тестовой выборке:   {scores[0]:.4f}")

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Обучение')
plt.plot(history.history['val_accuracy'], label='Валидация')
plt.title('Точность модели')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Обучение')
plt.plot(history.history['val_loss'], label='Валидация')
plt.title('Функция потерь')
plt.xlabel('Эпоха')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()