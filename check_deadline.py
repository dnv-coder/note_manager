# Grade 1. Этап 2: Задание 3

# Проверка дедлайна реализована в строках 67-76

from datetime import datetime, date

print("Grade 1. Этап 2: Задание 3")
print()

# Создаем переменные. Значения вводит пользователь
username = input("Введите имя пользователя: ")

# Создаем пустой список заголовков
titles = []

print("Введите заголовки заметки. Чтобы завершить ввод, нажмите 'Enter' на пустой строке")

# Запускаем цикл while True, в котором пользователь вводит заголовки
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
    user_date = input("Введите дату истечения срока действия заметки в формате 'день.месяц.год' (например, 22.12.2024): ")

    try:
        issue_date = datetime.strptime(user_date, "%d.%m.%Y").date()
        break
    except ValueError:
        print("Введенная дата не соответствует ожидаемому формату. Попробуйте снова.")

# Создаем словарь с данными
note = {
    "Имя пользователя": username,
    "Заголовки заметки": titles,
    "Описание заметки": content,
    "Статус заметки": status,
    "Дата создания": created_date,
    "Дата истечения заметки": issue_date,
}

# Функция форматированного вывода
def print_note(note):
    for key, value in note.items():
        if isinstance(value, list):
            print(f"{key}:")
            for i, item in enumerate(value, start=1):
                print(f"  {i}. {item}")
        elif isinstance(value, (date, datetime)):
            print(f"{key}: {value.strftime('%d.%m.%Y')}")
        else:
            print(f"{key}: {value}")

# Вывод заметки
print("\nДетали заметки:")
print_note(note)

# Проверка дедлайна
print("\nПроверка дедлайна:")
if issue_date < date.today():
    days_overdue = (date.today() - issue_date).days
    print(f"Внимание! Срок выполнения заметки истёк {days_overdue} дн. назад.")
elif issue_date == date.today():
    print("Срок выполнения заметки - сегодня.")
else:
    days_remaining = (issue_date - date.today()).days
    print(f"До истечения срока выполнения заметки остаётся {days_remaining} дн.")

# Отображаем текущий статус
print("\nВаш текущий статус заметки:", status)

# Список допустимых статусов
valid_status = ["выполнено", "в процессе", "отложено"]

# Ввод нового статуса
print("\nВозможные статусы: выполнено, в процессе, отложено")
while True:
    new_status = input("Введите новый статус: ").lower()
    if new_status in valid_status:
        print(f"\nВаш новый статус заметки: {new_status}")
        break
    else:
        print("Некорректный статус! Пожалуйста, введите из предложенных:", ", ".join(valid_status))
