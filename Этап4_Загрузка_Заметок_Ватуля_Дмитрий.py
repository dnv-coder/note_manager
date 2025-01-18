def load_notes_from_file(filename):
    """
    Читает заметки из текстового файла и преобразует их в список словарей.

    :param filename: Имя файла с заметками.
    :return: Список заметок в виде словарей.
    """
    notes = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            note_data = {}
            for line in file:
                line = line.strip()
                if line == "---":  # Разделитель между заметками
                    if note_data:
                        notes.append(note_data)
                        note_data = {}
                elif line:  # Обработка строк с данными
                    key, value = map(str.strip, line.split(":", 1))
                    # Преобразование ключей в английский стиль
                    key_mapping = {
                        "Имя пользователя": "username",
                        "Заголовок": "title",
                        "Описание": "content",
                        "Статус": "status",
                        "Дата создания": "created_date",
                        "Дедлайн": "issue_date",
                    }
                    if key in key_mapping:
                        note_data[key_mapping[key]] = value
            if note_data:  # Добавляем последнюю заметку
                notes.append(note_data)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return notes

# Пример использования
filename = "notes.txt"
loaded_notes = load_notes_from_file(filename)

if loaded_notes:
    print("Загруженные заметки:")
    for note in loaded_notes:
        print(note)
else:
    print("Нет заметок для загрузки.")
