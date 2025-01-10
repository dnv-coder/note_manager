# Grade 1. Этап 3: Задание 2

print("Grade 1. Этап 3: Задание 2")
print()

from datetime import date, datetime


def update_note(note):
    # Список допустимых полей для обновления
    updatable_fields = [
        "Имя пользователя",
        "Заголовок заметки",
        "Описание заметки",
        "Статус заметки",
        "Срок истечения заметки"
    ]

    # Выводим информацию о текущей заметке и доступных полях один раз
    print("Текущая заметка:")
    for key, value in note.items():
        if isinstance(value, date):  # Если значение - дата, форматируем её
            print(f"{key}: {value.strftime('%d.%m.%Y')}")
        else:
            print(f"{key}: {value}")
    print()

    print("Поля, доступные для обновления:", ", ".join(updatable_fields))
    print()

    # Запускаем цикл обновления полей
    while True:
        # Пользователь выбирает поле для обновления
        field = input("Введите поле для обновления: ").strip().capitalize()
        if field not in updatable_fields:
            print("Некорректное имя поля. Попробуйте снова.")
            continue
        print()
        # Пользователь вводит новое значение
        new_value = input(f"Введите новое значение для поля '{field}': ").strip().capitalize()

        # Проверяем формат даты, если поле - срок истечения заметки
        if field == "Срок истечения заметки":
            try:
                new_value = datetime.strptime(new_value, "%d.%m.%Y").date()
            except ValueError:
                print("Неверный формат даты. Дата должна быть в формате дд.мм.гггг.")
                continue

        # Обновляем поле в заметке
        note[field] = new_value
        print(f"Поле '{field}' успешно обновлено!")

        # Спрашиваем, нужно ли изменить что-то еще
        more_changes = input("Хотите обновить что-то еще? (да/нет): ").strip().lower()
        if more_changes != "да":
            break

    return note


# Пример заметки
example_note = {
    "Имя пользователя": "Иван",
    "Заголовок заметки": "Покупки",
    "Описание заметки": "Купить продукты",
    "Статус заметки": "в процессе",
    "Срок истечения заметки": date(2025, 1, 15)
}

# Вызов функции
updated_note = update_note(example_note)
print("Обновленная заметка:")
for key, value in updated_note.items():
    if isinstance(value, date):
        print(f"{key}: {value.strftime('%d.%m.%Y')}")
    else:
        print(f"{key}: {value}")
