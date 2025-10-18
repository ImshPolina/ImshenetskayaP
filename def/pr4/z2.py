A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    print(*range(A, B + 1))
else:
    print(*range(A, B - 1, -1))