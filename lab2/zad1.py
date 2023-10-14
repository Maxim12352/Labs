import math

# Зчитуємо значення α з клавіатури
alpha = float(input("Введіть значення α в радіанах: "))

# Обчислюємо z
z = math.cos(2 * alpha) + math.cos(4 * alpha)

# Виводимо результат
print(f"z = {z}")
