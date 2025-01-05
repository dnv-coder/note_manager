# Grade 1. Этап 2: Задание 1
print("Grade 1. Этап 2: Задание 1")

# Создаем пустой список
titles = []

print("Введите заголовки заметки. Чтобы завершить ввод, нажмите 'Enter' на пустой строке")

# Запускаем цикл while True, в котором пользователь вводит заголовки. Если переводится пустая строка, цикл прерывается.
while True:
    title = input("Введите заголовок: ")
    if title == "":
        break
    titles.append(title)

print()
print("Вы ввели следующие заголовки:")
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")
