from datetime import date
from note_manager.data.file_operations import save_notes_to_file, load_notes_from_file
import unittest
import os

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Определяем временный файл для тестов
        self.test_file = "test_notes.json"

    def tearDown(self):
        # Удаляем временный файл после тестов, если он существует
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        # Подготовка данных
        notes = [
            {
                "Имя пользователя": "Тест",
                "Заголовок": "Проверка",
                "Содержание": "Тестовое содержание",
                "Статус": "новая",
                "Дата создания": date(2025, 1, 1),
                "Дата истечения": date(2025, 1, 10),
            }
        ]

        # Сохранение в файл
        save_notes_to_file(notes, self.test_file)

        # Загрузка из файла
        loaded_notes = load_notes_from_file(self.test_file)

        # Проверка, что данные совпадают
        self.assertEqual(notes, loaded_notes)
