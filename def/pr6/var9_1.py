N = int(input("Введите количество элементов массива N: "))

arr = []
print(f"Введите {N} вещественных элементов массива:")
for i in range(N):
    element = float(input(f"Элемент [{i}]: "))
    arr.append(element)

print("\n" + "="*40)

print("Исходный массив:")
for i in range(N):
    print(f"[{i}] = {arr[i]}")

print("\n" + "="*40)

min_abs_element = arr[0]
min_abs_index = 0

for i in range(1, N):
    if abs(arr[i]) < abs(min_abs_element):
        min_abs_element = arr[i]
        min_abs_index = i

print(f"Минимальный по модулю элемент: {min_abs_element}")
print(f"Его индекс: {min_abs_index}")
print(f"Модуль элемента: {abs(min_abs_element)}")

print("\n" + "="*40)

print("Массив в обратном порядке:")
for i in range(N-1, -1, -1):

    print(f"[{N-1-i}] = {arr[i]}")
