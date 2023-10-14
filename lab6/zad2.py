def search_first_five_minimals(lst):
    # Перевіряємо, чи список має не менше п'яти елементів
    if len(lst) < 5:
        return "Список має менше п'яти елементів"

    # Сортуємо список у порядку зростання
    sorted_list = sorted(lst)

    # Вибираємо перші п'ять елементів з відсортованого списку
    first_five = sorted_list[:5]

    return first_five

# Зчитуємо список з клавіатури
input_list = input("Введіть список елементів через пробіл: ").split()

# Конвертуємо введений список до типу int (або float, залежно від типу елементів)
input_list = [int(item) for item in input_list]

# Викликаємо функцію для пошуку перших п'яти мінімальних елементів
first_five_minimals = search_first_five_minimals(input_list)

# Виводимо результат на екран
print("Перші п'ять мінімальних елементів:", first_five_minimals)
