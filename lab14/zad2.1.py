import matplotlib.pyplot as plt

# Дані для України та США (припустимо, що ми вже отримали ці дані)
years = [2000, 2005, 2010, 2015, 2020]  # Роки
ukraine_data = [5, 4, 3, 2, 1]  # Дані для України (припустимі значення)
usa_data = [1, 2, 2, 1, 1]  # Дані для США (припустимі значення)

# Побудова графіків
plt.plot(years, ukraine_data, label='Україна')
plt.plot(years, usa_data, label='США')

# Позначення осей та заголовок графіка
plt.xlabel('Рік')
plt.ylabel('Children out of school, primary')
plt.title('Динаміка показника "Children out of school, primary"')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.show()
