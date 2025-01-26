from note_manager.data import load_notes_from_file, save_notes_to_file
from note_manager.interface import (
    display_menu,
    add_note_interface,
    view_notes_interface,
    update_note_interface,
    delete_note_interface,
    search_notes_interface,
)


def main():
    filename = "notes.json"
    # Загрузить заметки из файла, если файл существует
    try:
        notes = load_notes_from_file(filename)
    except FileNotFoundError:
        notes = []
        print(f"Файл {filename} не найден. Будет создан новый файл при сохранении заметок.")
        save_notes_to_file(notes, filename)  # Создать файл

    while True:
        display_menu()
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            add_note_interface(notes, filename)
        elif choice == "2":
            view_notes_interface(notes)
        elif choice == "3":
            update_note_interface(notes, filename)
        elif choice == "4":
            delete_note_interface(notes, filename)
        elif choice == "5":
            search_notes_interface(notes)
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

        # Сохранить заметки после выполнения каждой операции
        save_notes_to_file(notes, filename)


if __name__ == "__main__":
    main()

