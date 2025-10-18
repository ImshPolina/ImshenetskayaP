A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A > B:
    print(f"Нечётные числа от {A} до {B} в порядке убывания:")
    for i in range(A, B - 1, -1):
        if i % 2 != 0:
            print(i, end=" ")
else:
    print("Ошибка: A должно быть > B")