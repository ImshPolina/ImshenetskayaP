number = int(input("Введите двузначное число: "))
if 10 <= number <= 99:
    
    first_digit = number // 10
    second_digit = number % 10
    
    if first_digit == second_digit:
        print("Да")
    else:
        print("Нет")
else:
    print("Ошибка! Введите двузначное число.")