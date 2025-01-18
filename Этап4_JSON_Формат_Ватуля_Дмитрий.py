import json

def save_notes_json(notes, filename):
    """
    Сохраняет список заметок в формате JSON в указанный файл.

    :param notes: Список заметок, где каждая заметка представлена как словарь.
    :param filename: Имя файла для сохранения заметок.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Сериализация данных в JSON-формат с отступами
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(f"Заметки успешно сохранены в файл '{filename}'.")
    except Exception as e:
        print(f"Ошибка при сохранении заметок: {e}")


# Пример использования функции
notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    },
    {
        "username": "Мария",
        "title": "Встреча",
        "content": "Встретиться с друзьями",
        "status": "в процессе",
        "created_date": "26-11-2024",
        "issue_date": "29-11-2024"
    }
]

filename = "_notes.json"
save_notes_json(notes, filename)
