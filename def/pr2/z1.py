import math

x = 14.26
y = -1.22
z = 3.5e-2

numerator = 2 * math.cos(x - 2/3)
denominator = 1/2 + math.sin(y)**2
fraction = numerator / denominator

z_numerator = z**2
z_denominator = 3 - z**2 / 5
z_fraction = 1 + z_numerator / z_denominator

s = fraction * z_fraction

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"s = {s:.6f}")