n = int(input())
a, b, total = 0, 1, 0

for i in range(n):
    total += a
    a, b = b, a + b

print(total)