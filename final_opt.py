# Grade 1. Этап 1. Задание 5
print("Grade 1. Этап 1. Задание 5")
print()

# Импортируем текущую дату
from datetime import datetime, date

# Создаем переменные. Значения вводит пользователь
username = input("Введите имя пользователя: ")
title_1 = input("Введите название первого раздела: ")
title_2 = input("Введите название второго раздела: ")
title_3 = input("Введите название третьего раздела: ")
content = input("Введите описание заметки: ")
status = input("Введите предпочитаемый статус заметки (например, 'в работе') ")

# Получаем текущую дату
created_date = date.today()

# спрашиваем у пользователя дедлайн заметки

while True:
    user_date = input("Введите дату истечения срока действия заметки в формате 'день.месяц.год' (например, 22.12.2024) ")

    try:
        issue_date = datetime.strptime(user_date, "%d.%m.%Y").date()
        if issue_date > date.today():
            break
        else:
            print("Дата истечения должна быть позже текущей даты.")
    except ValueError:
        print("Введенная дата не соответствует ожидаемому формату")

#Создаем словарь с данными
note = {"Имя пользователя": username,
        "Заголовки заметки": [title_1, title_2, title_3],
        "Описание заметки": content,
        "Статус заметки": status,
        "Дата создания": created_date,
        "Дата истечения заметки": issue_date
        }
# Функция форматированного вывода
print()
def print_note(note):
    for key, value in note.items():
        if isinstance(value, list):
            print(f"{key}")
            for i, item in enumerate(value, start=1):
                print(f"  {i}. {item}")
        elif isinstance(value, (date, datetime)):
            print(f"{key}: {value.strftime('%d.%m')}")
        else:
            print(f"{key}: {value}")

# Вывод
print_note(note)



