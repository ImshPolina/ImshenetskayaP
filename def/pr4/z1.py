A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A <= B:
    print(f"Все числа от {A} до {B} включительно:")

    for i in range(A, B + 1):
        print(i, end=" ")
else:
    print("Ошибка: A должно быть ≤ B")