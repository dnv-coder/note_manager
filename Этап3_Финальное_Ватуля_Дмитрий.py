# Grade 1. Этап 3: Финальное задание
# Добавляем функцию интерактивного меню

print("Grade 1. Этап 3: Финальное задание")

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

# Функция обновления заметки
def update_note():
    if not notes:
        print("Список заметок пуст. Нечего обновлять.")
        print()
        return

    # Отображаем все заметки с порядковыми номерами
    print("Список заметок:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['Заголовок']} (Пользователь: {note['Имя пользователя']})")
    print()

    # Запрашиваем номер заметки для обновления
    while True:
        try:
            choice = int(input("Введите номер заметки, которую хотите обновить: "))
            if 1 <= choice <= len(notes):
                selected_note = notes[choice - 1]
                break
            else:
                print("Некорректный номер. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Введите число.")

    # Отображаем выбранную заметку
    print("Вы выбрали следующую заметку:")
    for key, value in selected_note.items():
        if isinstance(value, date):
            print(f"{key}: {value.strftime('%d.%m.%Y')}")
        else:
            print(f"{key}: {value}")
    print()

    # Список полей, которые можно обновить
    updatable_fields = ["Имя пользователя", "Заголовок", "Содержание", "Статус", "Дата истечения"]

    print("Поля, доступные для обновления: ", ", ".join(updatable_fields))

    # Выбор поля для обновления
    while True:
        field = input("Введите поле, которое хотите обновить: ").strip().capitalize()
        if field not in updatable_fields:
            print("Некорректное поле. Попробуйте снова.")
        else:
            break

    # Запрашиваем новое значение для выбранного поля
    new_value = input(f"Введите новое значение для поля '{field}': ").strip()

    # Проверяем формат даты, если обновляется "Дата истечения"
    if field == "Дата истечения":
        try:
            new_value = datetime.strptime(new_value, "%d.%m.%Y").date()
        except ValueError:
            print("Неверный формат даты. Обновление отменено.")
            return

    # Обновляем выбранное поле в заметке
    selected_note[field] = new_value
    print(f"Поле '{field}' успешно обновлено!")
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

# Функция поиска заметок по ключевому слову и/или статусу
def search_notes(notes, keyword=None, status=None):
    if not notes:
        print("Список заметок пуст.")
        print()
        return

    # Фильтруем заметки по критериям
    filtered_notes = []
    for note in notes:
        if keyword and not any(keyword.lower() in str(value).lower() for value in note.values()):
            continue
        if status and note.get("Статус") != status:
            continue
        filtered_notes.append(note)

    # Вывод результатов поиска
    if filtered_notes:
        print("Результаты поиска:")
        print()
        for i, note in enumerate(filtered_notes, start=1):
            print(f"Заметка {i}:")
            for key, value in note.items():
                if isinstance(value, date):
                    print(f"{key}: {value.strftime('%d.%m.%Y')}")
                else:
                    print(f"{key}: {value}")
            print()
    else:
        print("Нет заметок, соответствующих критериям поиска.")
        print()

# Функция для получения критериев поиска
def get_search_criteria():
    print("Вы можете искать заметки по ключевому слову и/или статусу.")
    keyword = input("Введите ключевое слово для поиска (или оставьте пустым): ").strip()
    status = input("Введите статус заметки для поиска (или оставьте пустым): ").strip()
    if not keyword:
        keyword = None
    if not status:
        status = None
    return keyword, status


# Цикл для управления добавлением, просмотром, удалением и поиском заметок

while True:
    print("Меню:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Искать заметки")
    print("6. Выйти")
    print()

    choice = input("Введите номер действия: ")
    print()

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        update_note()
    elif choice == "4":
        criteria = get_deletion_criteria()
        notes = delete_notes(notes, criteria)
    elif choice == "5":
        keyword, status = get_search_criteria()
        search_notes(notes, keyword, status)
    elif choice == "6":
        print("Программа завершена.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
