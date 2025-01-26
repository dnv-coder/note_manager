from datetime import date
from data.file_operations import save_notes_to_file
from utils.helpers import validate_date, validate_status, generate_unique_id

def display_menu():
    print("\nМеню:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Искать заметки")
    print("6. Выйти")
    print()

def add_note_interface(notes, filename):
    print("Добавление новой заметки:")
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")

    while True:
        status = input("Введите статус заметки (например, 'новая', 'в процессе', 'выполнена'): ")
        status = validate_status(status)
        if status:
            break
        print("Некорректный статус. Допустимые значения: 'новая', 'в процессе', 'выполнена'.")

    created_date = date.today()

    while True:
        issue_date_str = input("Введите дату истечения (день.месяц.год): ")
        issue_date = validate_date(issue_date_str)
        if issue_date:
            break
        print("Неверный формат даты. Попробуйте снова.")

    note = {
        "ID": generate_unique_id(),
        "Имя пользователя": username,
        "Заголовок": title,
        "Содержание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дата истечения": issue_date,
    }

    notes.append(note)
    save_notes_to_file(notes, filename)
    print("Заметка успешно добавлена!")

def view_notes_interface(notes):
    if not notes:
        print("Список заметок пуст.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"Заметка {i}:")
        for key, value in note.items():
            print(f"{key}: {value}")
        print()

def update_note_interface(notes, filename):
    if not notes:
        print("Список заметок пуст. Нечего обновлять.")
        return

    view_notes_interface(notes)
    try:
        index = int(input("Введите номер заметки, которую хотите обновить: ")) - 1
        if 0 <= index < len(notes):
            note = notes[index]
            print("Обновление заметки. Если не хотите менять поле, оставьте его пустым.")
            note["Имя пользователя"] = input(f"Имя пользователя [{note['Имя пользователя']}]: ") or note["Имя пользователя"]
            note["Заголовок"] = input(f"Заголовок [{note['Заголовок']}]: ") or note["Заголовок"]
            note["Содержание"] = input(f"Содержание [{note['Содержание']}]: ") or note["Содержание"]

            while True:
                status = input(f"Статус [{note['Статус']}]: ") or note["Статус"]
                validated_status = validate_status(status)
                if validated_status:
                    note["Статус"] = validated_status
                    break
                print("Некорректный статус. Попробуйте снова.")

            while True:
                issue_date_str = input(f"Дата истечения [{note['Дата истечения']}]: ")
                if not issue_date_str:
                    break
                issue_date = validate_date(issue_date_str)
                if issue_date:
                    note["Дата истечения"] = issue_date
                    break
                print("Неверный формат даты. Попробуйте снова.")

            save_notes_to_file(notes, filename)
            print("Заметка успешно обновлена!")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")

def delete_note_interface(notes, filename):
    if not notes:
        print("Список заметок пуст. Нечего удалять.")
        return

    view_notes_interface(notes)
    try:
        index = int(input("Введите номер заметки, которую хотите удалить: ")) - 1
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            save_notes_to_file(notes, filename)
            print(f"Заметка '{deleted_note['Заголовок']}' успешно удалена!")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")


def search_notes_interface(notes):
    if not notes:
        print("Список заметок пуст. Нечего искать.")
        return

    query = input("Введите текст для поиска по заголовку или содержанию: ").strip().lower()
    results = [
        note for note in notes
        if query in note["Заголовок"].lower() or query in note["Содержание"].lower()
    ]

    if results:
        print(f"Найдено {len(results)} заметок:")
        for i, note in enumerate(results, start=1):
            print(f"Заметка {i}:")
            for key, value in note.items():
                print(f"{key}: {value}")
            print()
    else:
        print("Совпадений не найдено.")
