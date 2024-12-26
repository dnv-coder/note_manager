# Grade 1. Этап 1. Задание 4
print("Grade 1. Этап 1. Задание 4")
print()

# Создаем переменные. Значения вводит пользователь
username = input("Введите имя пользователя: ")
title_1 = input("Введите первый заголовок: ")
title_2 = input("Введите второй заголовок: ")
title_3 = input("Введите третий заголовок: ")
content = input("Введите описание заметки: ")
status = input("Введите предпочитаемый статус заметки (например, 'в работе') ")

#создаем список из заголовков
title = [title_1, title_2, title_3]

# импортируем текущую дату и присваиваем ее значение переменной
from datetime import *
created_date = date.today()

# спрашиваем у пользователя дедлайн заметки
# преобразуем введенную пользователем дату в объект даты

while True:
    user_date = input("Введите дату истечения срока действия заметки в формате 'день.месяц.год' (например, 22.12.2024) ")

    try:
        issue_date = datetime.strptime(user_date, "%d.%m.%Y")
        break
    except ValueError:
        print("Введенная дата не соответствует ожидаемому формату")

#Выводим значения переменных
print()
print("Имя пользователя: ", username)
print(f"Заголовки заметки: {title[0]}, {title[1]}, {title[2]}")
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date.strftime("%d.%m"))
print("Дата истечения заметки: ", issue_date.strftime("%d.%m"))

