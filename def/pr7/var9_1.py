def sum_of_digits(n):
    total = 0
    num = abs(n)  # работаем с модулем числа для отрицательных чисел
    while num > 0:
        total += num % 10  # получаем последнюю цифру
        num //= 10         # удаляем последнюю цифру
    return total

def count_operations_to_zero(n):
    if n == 0:
        return 0
    
    count = 0
    current = n
    
    print(f"Начальное число: {n}")
    print("\nПроцесс вычислений:")
    
    while current > 0:
        digits_sum = sum_of_digits(current)
        next_value = current - digits_sum
        print(f"Шаг {count + 1}: {current} - {digits_sum} = {next_value}")
        current = next_value
        count += 1
    
    return count

print("=== ПОДСЧЕТ КОЛИЧЕСТВА ОПЕРАЦИЙ ДО НУЛЯ ===")
try:
    number = int(input("Введите целое число: "))
    
    if number < 0:
        print("Введите положительное число!")
    else:
        operations = count_operations_to_zero(number)
        print(f"\nРезультат: число {number} станет нулём через {operations} операций")
        
except ValueError:
    print("Ошибка! Введите целое число.")