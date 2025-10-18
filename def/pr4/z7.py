n = int(input("Введите натуральное число n: "))

total = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i  
    total += factorial

print(f"Сумма 1! + 2! + 3! + ... + {n}! = {total}")