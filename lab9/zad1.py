# a) Створення текстового файлу TF7_1
with open("TF7_1.txt", "w", encoding="utf-8") as file:
    file.write("Це є рядок з подвоєними буквами та числами: слово слово слово 123 456 789\n")
    file.write("Цей рядок містить числа: 1234 5678 9\n")
    file.write("А от ця фраза не має подвоєнь і містить числа: програмування 11 22 33\n")

# b) Знаходження та запис слів з подвоєнням в інший файл TF7_2
with open("TF7_1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

duplicated_words = []
for line in lines:
    words = line.split()
    for word in words:
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                duplicated_words.append(word)
                break

with open("TF7_2.txt", "w", encoding="utf-8") as file:
    if duplicated_words:
        for word in duplicated_words:
            file.write(word + "\n")
    else:
        file.write("Немає слів із подвоєнням букв\n")

# c) Виведення вмісту файлу TF7_2 по рядках
with open("TF7_2.txt", "r", encoding="utf-8") as file:
    print("Вміст файлу TF7_2:")
    for line in file:
        print(line.strip())
