# Grade 1. Этап 3: Задание 3
# Добавляем функцию форматированного вывода всех заметок

print("Grade 1. Этап 3: Задание 3")

notes = []  # Список для хранения всех заметок

from datetime import date, datetime

# Функция добавления новой заметки
def add_note():
    print("Добавление новой заметки:")
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    status = input("Введите статус заметки (например, 'выполнено', 'в процессе'): ")

    created_date = date.today()

    while True:
        try:
            issue_date = input("Введите дату истечения срока действия заметки (день.месяц.год): ")
            issue_date = datetime.strptime(issue_date, "%d.%m.%Y").date()
            print()
            break
        except ValueError:
            print("Неверный формат даты. Попробуйте снова.")

    note = {
        "Имя пользователя": username,
        "Заголовок": title,
        "Содержание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дата истечения": issue_date
    }

    notes.append(note)  # Добавляем заметку в общий список
    print("Заметка успешно добавлена!")
    print()

# Функция отображения всех заметок
def view_notes():
    if not notes:
        print("Список заметок пуст.")
        print()
        return

    print("Список всех заметок:")
    print()
    for i, note in enumerate(notes, start=1):
        print(f"Заметка {i}:")
        for key, value in note.items():
            if isinstance(value, date):
                print(f"{key}: {value.strftime('%d.%m.%Y')}")
            else:
                print(f"{key}: {value}")
        print()

# Задаем критерии удаления заметки
def get_deletion_criteria():
    print("Вы можете удалить заметку по имени пользователя или заголовку.")
    return input("Введите имя пользователя или заголовок заметки для удаления: ").strip()

# Задаем функцию удаления заметок
def delete_notes(notes, criteria):
    initial_length = len(notes)
    notes = [note for note in notes if note['Имя пользователя'] != criteria and note['Заголовок'] != criteria]

    if len(notes) < initial_length:
        print()
        print(f"Заметки, соответствующие критерию '{criteria}', успешно удалены.")
        print()
    else:
        print(f"Заметок, соответствующих критерию '{criteria}', не найдено.")
        print()

    return notes

# Цикл для управления добавлением, просмотром заметок, удалением заметок
while True:
    print("Меню:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Удалить заметку")
    print("4. Выйти")
    print()

    choice = input("Введите номер действия: ")
    print()

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        criteria = get_deletion_criteria()
        notes = delete_notes(notes, criteria)
    elif choice == "4":
        print("Программа завершена.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
