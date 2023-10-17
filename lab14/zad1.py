import numpy as np
import matplotlib.pyplot as plt

# Створення значень x в діапазоні [0, 5]
x = np.linspace(0, 5, 1000)

# Обчислення відповідних значень Y(x)
y = np.sqrt(x) * np.sin(10 * x)

# Побудова графіка
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x) = x^(1/2) * sin(10x)')

# Позначення осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Встановлення обмежень на вісі y для кращого вигляду графіка
plt.ylim(-2, 2)

# Виведення легенди
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()
