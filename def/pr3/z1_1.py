a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

print("Числа, принадлежащие интервалу [1, 3]:")
found = False
for num in [a, b, c]:
    if 1 <= num <= 3:
        print(num)
        found = True

if not found:
    print("Таких чисел нет")
