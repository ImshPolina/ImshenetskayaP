def calculate_expression(x, n):
    
    if n == 0:
        return 1.0
    
    return (x / n) * calculate_expression(x, n - 1)
    
if __name__ == "__main__":

    print("Тест 1: 2^3/3! =", calculate_expression(2, 3))
    print("Тест 2: 5^0/0! =", calculate_expression(5, 0))
    print("Тест 3: 3^1/1! =", calculate_expression(3, 1))
    print("Тест 4: 4^2/2! =", calculate_expression(4, 2))
    print("Тест 5: 1^5/5! =", calculate_expression(1, 5))
    
    print("\nПроверка математических свойств:")
    print("e ≈ 2.71828, вычисляем через ряд: e^x = Σ(x^n/n!)")
    print("Для x=1, первые 10 членов ряда:")
    
    sum_e = 0
    for n in range(10):
        term = calculate_expression(1, n)
        sum_e += term
        print(f"  n={n}: 1^{n}/{n}! = {term}")
    
    print(f"Сумма первых 10 членов: {sum_e}")
    print(f"Приближение к e: {sum_e}")