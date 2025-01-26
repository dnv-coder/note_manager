import json
from datetime import datetime

def save_notes_to_file(notes, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4, default=str)

def load_notes_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = json.load(f)
            for note in notes:
                note["Дата создания"] = datetime.strptime(note["Дата создания"], "%Y-%m-%d").date()
                note["Дата истечения"] = datetime.strptime(note["Дата истечения"], "%Y-%m-%d").date()
            return notes
    except FileNotFoundError:
        # Если файл отсутствует, возвращаем пустой список
        raise FileNotFoundError(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        # Если файл поврежден или пустой, возвращаем пустой список
        print(f"Файл {filename} поврежден или пуст. Будет создан новый файл.")
        return []
    except Exception as e:
        # Для всех остальных ошибок выбрасываем RuntimeError
        raise RuntimeError(f"Ошибка при загрузке заметок: {e}")


