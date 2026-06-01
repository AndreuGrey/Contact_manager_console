# Основной файл для меню
import contacts as con


def clear_terminal():  # Очищает терминал в VS Code
    print("\033[H\033[J", end="")


def menu_admin():  # Выводит список доступных команд
    menu_admin = [
        '1. Список контактов',
        '2. Добавить контакт',
        '3. Изменить контакт',
        '4. Удалить контакт',
        '5. Закрыть программу'
    ]

    print()
    for i in menu_admin:
        print(i)


def programm_operation():  # Основная логика программы!
    menu_admin()
    command = int(input(f"\nВведите команду: "))
    if command == 1:  # Список контактов
        clear_terminal()
        con.output_ten_contacts()
    elif command == 2:  # Добавить контакт
        clear_terminal()
        con.add_contact_important()
    elif command == 3:  # Изменить контакт
        clear_terminal()
        con.change_of_contact()
    elif command == 4:  # Удалить контакт
        clear_terminal()
        con.delete_contact()
    elif command == 5:  # Закрыть программу
        clear_terminal()
        con.close_connection()
        exit()
    else:
        clear_terminal()
        print('Такой команды не существует!')


while True:
    programm_operation()
