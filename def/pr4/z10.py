n = int(input("Введите количество чисел N: "))
k = int(input("Введите начальный номер K: "))

a, b = 0, 1
fib_sum = 0
current_position = 1

# Проходим по всем числам Фибоначчи
while current_position <= k + n - 1:
    # Если текущая позиция >= K, добавляем к сумме
    if current_position >= k:
        fib_sum += a
    
    # Переход к следующему числу
    a, b = b, a + b
    current_position += 1

print(fib_sum)