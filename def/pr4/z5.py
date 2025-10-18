n = int(input("Введите натуральное число n: "))

total = 0
for i in range(1, n + 1):
    total += i ** 3

print(f"Сумма 1³ + 2³ + 3³ + ... + {n}³ = {total}")