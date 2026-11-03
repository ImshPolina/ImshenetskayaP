# ============================================================
# ПРАКТИЧЕСКАЯ РАБОТА №3 — ВАРИАНТ 1
# Анализ качества обучения НС при разных функциях потерь:
#  1. бинарная кросс-энтропия (binary crossentropy)
#  2. категориальная кросс-энтропия (categorical crossentropy)
#  3. средний квадрат ошибок (mean squared error)
# ============================================================

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(42)
tf.random.set_seed(42)

print("=" * 60)
print("ЗАГРУЗКА ДАННЫХ CIFAR-10")
print("=" * 60)

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

train_labels_cat = to_categorical(train_labels, 10)
test_labels_cat = to_categorical(test_labels, 10)

perm = np.random.permutation(len(train_images))
train_images = train_images[perm]
train_labels_cat = train_labels_cat[perm]

val_images = train_images[:15000]
val_labels = train_labels_cat[:15000]
train_images_new = train_images[15000:]
train_labels_new = train_labels_cat[15000:]

print(f"Обучающая выборка:    {train_images_new.shape}")
print(f"Валидационная выборка: {val_images.shape}")
print(f"Тестовая выборка:     {test_images.shape}")

def build_model(loss_fn):
    """
    Строит свёрточную НС с минимальным числом нейронов,
    достаточным для классификации CIFAR-10 на уровне ≥92%.
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    return model

print("\n" + "=" * 60)
print("ЗАДАНИЕ 1 (ВАРИАНТ 1): АНАЛИЗ ФУНКЦИЙ ПОТЕРЬ")
print("=" * 60)

EPOCHS = 15
BATCH_SIZE = 64

losses = {
    'binary_crossentropy':      'binary_crossentropy',
    'categorical_crossentropy': 'categorical_crossentropy',
    'mean_squared_error':       'mean_squared_error'
}

histories = {}
results = {}

for name, loss_fn in losses.items():
    print(f"\n--- Обучение с loss = {name} ---")
    model = build_model(loss_fn)
    start = time.time()
    history = model.fit(
        train_images_new, train_labels_new,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_data=(val_images, val_labels),
        verbose=2
    )
    elapsed = time.time() - start
    test_loss, test_acc = model.evaluate(test_images, test_labels_cat, verbose=0)
    histories[name] = history
    results[name] = {'acc': test_acc, 'loss': test_loss, 'time': elapsed}
    print(f"Результат: test_acc = {test_acc:.4f}, test_loss = {test_loss:.4f}, "
          f"время = {elapsed:.1f} c")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for name, h in histories.items():
    axes[0].plot(h.history['accuracy'], label=f'{name} (train)')
    axes[0].plot(h.history['val_accuracy'], '--', label=f'{name} (val)')
    axes[1].plot(h.history['loss'], label=f'{name} (train)')
    axes[1].plot(h.history['val_loss'], '--', label=f'{name} (val)')

axes[0].set_title('Accuracy по эпохам')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].legend(fontsize=8)
axes[0].grid(True)

axes[1].set_title('Loss по эпохам')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].legend(fontsize=8)
axes[1].grid(True)

plt.tight_layout()
plt.savefig('variant1_losses.png', dpi=120)
plt.show()

print("\n" + "=" * 60)
print("ИТОГОВАЯ ТАБЛИЦА ПО ВАРИАНТУ 1")
print("=" * 60)
print(f"{'Функция потерь':<30} {'Test Acc':<12} {'Test Loss':<12} {'Время, с':<10}")
print("-" * 64)
for name, r in results.items():
    print(f"{name:<30} {r['acc']:<12.4f} {r['loss']:<12.4f} {r['time']:<10.1f}")

best_name = max(results, key=lambda k: results[k]['acc'])
print(f"\nЛучшая функция потерь: {best_name} "
      f"(accuracy = {results[best_name]['acc']:.4f})")
if results[best_name]['acc'] >= 0.92:
    print("Требование ≥92% на тестовой выборке ВЫПОЛНЕНО ✓")
else:
    print("Требование ≥92% НЕ достигнуто — увеличьте EPOCHS или усложните архитектуру.")