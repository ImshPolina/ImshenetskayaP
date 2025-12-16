print("\n" + "="*50)

A = []
B = []

print("Введите 10 элементов для массива A:")
for i in range(10):
    element = float(input(f"A[{i}]: "))
    A.append(element)

print("\nВведите 10 элементов для массива B:")
for i in range(10):
    element = float(input(f"B[{i}]: "))
    B.append(element)

print("\n" + "="*40)

print("Исходный массив A:")
for i in range(10):
    print(f"A[{i}] = {A[i]}")

print("\nИсходный массив B:")
for i in range(10):
    print(f"B[{i}] = {B[i]}")

print("\n" + "="*40)

A, B = B, A  

print("После обмена содержимым:")
print("\nПреобразованный массив A:")
for i in range(10):
    print(f"A[{i}] = {A[i]}")

print("\nПреобразованный массив B:")
for i in range(10):

    print(f"B[{i}] = {B[i]}")

