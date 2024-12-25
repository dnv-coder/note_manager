# Grade 1. Этап 1. Задание 3
print("Grade 1. Этап 1. Задание 3")
print()

# Создаем переменные. Значения вводит пользователь
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите предпочитаемый статус заметки (например, 'в работе') ")

# импортируем текущую дату и присваиваем ее значение переменной
from datetime import date
created_date = date.today()

# спрашиваем у пользователя дедлайн заметки
# преобразуем введенную пользователем дату в объект даты
from datetime import datetime

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
print("Заголовок заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date.strftime("%d.%m"))
print("Дата истечения заметки: ", issue_date.strftime("%d.%m"))

