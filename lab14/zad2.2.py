import matplotlib.pyplot as plt

# Дані для України та США (припустимо, що ми вже отримали ці дані)
countries = ['Україна', 'США']
data = {}

# Запит користувача на вибір країни для побудови діаграми
selected_country = input('Введіть назву країни (Україна або США): ')

if selected_country not in countries:
    print('Неправильна назва країни.')
else:
    # Припустимі дані для кожної країни (можна замінити реальними даними)
    if selected_country == 'Україна':
        data = {
            '2000': 5,
            '2005': 4,
            '2010': 3,
            '2015': 2,
            '2020': 1
        }
    else:
        data = {
            '2000': 1,
            '2005': 2,
            '2010': 2,
            '2015': 1,
            '2020': 1
        }

    years = list(data.keys())
    values = list(data.values())

    # Побудова стовпчастої діаграми
    plt.bar(years, values)

    # Позначення осей та заголовок діаграми
    plt.xlabel('Рік')
    plt.ylabel('Children out of school, primary')
    plt.title(f'Показник для {selected_country}')

    # Відображення діаграми
    plt.show()
