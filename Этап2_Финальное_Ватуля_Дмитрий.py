#Этап2_Финальное_Ватуля_Дмитрий

print("Этап 2. Финальное задание. Ватуля Дмитрий")

from datetime import datetime

# Список заметок
notes = []

# Функция для добавления заголовков
def add_titles_loop():
    titles = []
    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ")
        if title == "":
            break
        titles.append(title)
    print("\nЗаголовки заметки:")
    for t in titles:
        print(f"- {t}")

# Функция для обновления статуса заметки
def update_status():
    statuses = ["выполнено", "в процессе", "отложено"]
    print("Текущий статус заметки: 'в процессе'")
    print("Выберите новый статус заметки:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(statuses):
                print(f"Статус заметки успешно обновлён на: '{statuses[choice - 1]}'")
                break
            else:
                print("Пожалуйста, выберите корректный номер из списка.")
        except ValueError:
            print("Введите число, соответствующее вашему выбору.")

# Функция для проверки дедлайна
def check_deadline():
    today = datetime.today()
    print(f"Текущая дата: {today.strftime('%d.%m.%Y')}")
    while True:
        deadline_str = input("Введите дату дедлайна (в формате день.месяц.год): ")
        try:
            deadline = datetime.strptime(deadline_str, "%d.%m.%Y")
            if deadline < today:
                days_overdue = (today - deadline).days
                print(f"Внимание! Дедлайн истёк {days_overdue} дней назад.")
            elif deadline > today:
                days_left = (deadline - today).days
                print(f"До дедлайна осталось {days_left} дней.")
            else:
                print("Дедлайн сегодня!")
            break
        except ValueError:
            print("Некорректный формат даты. Попробуйте снова.")

# Функция для добавления заметки
def add_note():
    global notes
    print("\nДобавление новой заметки:")
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")

    # Проверка и форматирование даты создания
    while True:
        creation_date = input("Введите дату создания (день.месяц.год): ")
        try:
            creation_date = datetime.strptime(creation_date, "%d.%m.%Y").strftime("%d.%m.%Y")
            break
        except ValueError:
            print("Некорректный формат даты. Попробуйте снова.")

    # Проверка и форматирование дедлайна
    while True:
        deadline = input("Введите дедлайн (день.месяц.год): ")
        try:
            deadline = datetime.strptime(deadline, "%d.%m.%Y").strftime("%d.%m.%Y")
            break
        except ValueError:
            print("Некорректный формат даты. Попробуйте снова.")

    note = {
        "Имя": user_name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline,
    }
    notes.append(note)
    print("Заметка успешно добавлена!\n")

# Функция для удаления заметки
def delete_note():
    global notes
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. Имя: {note['Имя']}, Заголовок: {note['Заголовок']}, Описание: {note['Описание']}")
    to_delete = input("Введите имя пользователя или заголовок для удаления заметки: ")
    updated_notes = [note for note in notes if note["Имя"] != to_delete and note["Заголовок"] != to_delete]
    if len(updated_notes) < len(notes):
        notes = updated_notes
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")

# Функция для вывода всех заметок
def show_notes():
    if not notes:
        print("Заметок пока нет.")
    else:
        print("\nСписок заметок:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. Имя: {note['Имя']}")
            print(f"   Заголовок: {note['Заголовок']}")
            print(f"   Описание: {note['Описание']}")
            print(f"   Статус: {note['Статус']}")
            print(f"   Дата создания: {note['Дата создания']}")
            print(f"   Дедлайн: {note['Дедлайн']}")
            print("-" * 20)

# Основная функция программы
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Добавить заголовки")
        print("3. Обновить статус заметки")
        print("4. Проверить дедлайн")
        print("5. Удалить заметку")
        print("6. Показать все заметки")
        print("7. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            add_titles_loop()
        elif choice == "3":
            update_status()
        elif choice == "4":
            check_deadline()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            show_notes()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
