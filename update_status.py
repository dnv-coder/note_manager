# Grade 1. Этап 2: Задание 2
from time import strftime

print("Grade 1. Этап 2: Задание 2")
print()

# Импортируем текущую дату
from datetime import datetime, date

# Создаем переменные. Значения вводит пользователь
username = input("Введите имя пользователя: ")

# Создаем пустой список заголовков
titles = []

print("Введите заголовки заметки. Чтобы завершить ввод, нажмите 'Enter' на пустой строке")

# Запускаем цикл while True, в котором пользователь вводит заголовки. Если переводится пустая строка, цикл прерывается.
while True:
    title = input("Введите заголовок: ")
    if title == "":
        break
    titles.append(title)

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
        elif issue_date == date.today():
            print("Дата истечения заметки - сегодня")
            break
        else:
            print("Дата истечения должна быть позже текущей даты.")
    except ValueError:
        print("Введенная дата не соответствует ожидаемому формату")

#Создаем словарь с данными
note = {"Имя пользователя": username,
        "Заголовки заметки": titles,
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

# Выводим заголовки
print()
print("Вы ввели следующие заголовки:")
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")

print("Возможные статусы: выполнено, в процессе, отложено")
print()

# Отображаем текущий статус
print(f"Ваш текущий статус вашей заметки: {status}")
print()

# Список допустимых статусов
valid_status = ["выполнено", "в процессе", "отложено"]

# Выводим пользователю список статусов
print("Выберите новый статус заметки из списка: ")
print(", ".join(valid_status))

# Ввод нового статуса
new_status = input("Введите новый статус: ")
print()

# Проверяем корректность ввода
while True:
    if new_status.lower() in valid_status:
        new_status = new_status.lower()
        break
    else:
        print("Некорректный статус! Пожалуйста, введите из предложенных: ")
        print(", ".join(valid_status))
        new_status = input("Введите новый статус: ")

#Выводим обновленный статус
print()
print(f"Ваш новый статус заметки: {new_status}")
print()

if issue_date < date.today():
    print("Время выполнения заметки истекло")
elif issue_date == date.today():
    print("Время выполнения заметки - сегодня")
else:
    print(f"Срок выполнения заметки: {issue_date.strftime('%d.%m')}")

if issue_date > date.today():
    days_remaining = (issue_date - date.today()).days
    print(f"До истечения срока выполнения зампетки остается: {days_remaining} д.")
