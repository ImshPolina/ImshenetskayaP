a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

if a < b:
    x = a + b
elif a > b:
    x = a - b
else:  # a == b
    x = 1

print(f"a = {a}")
print(f"b = {b}")
print(f"x = {x}")