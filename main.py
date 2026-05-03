# Основной файл для меню
import contacts as con


def clear_terminal():  # Очищает терминал в VS Code
    print("\033[H\033[J", end="")


def menu_output():  # Выводит список доступных команд
    menu = [
        '1. Список контактов',
        '2. Добавить контакт',
        '3. Изменить контакт',
        '4. Удалить контакт',
        '5. Закрыть программу'
    ]

    for i in menu:
        print(i)


def programm_operation():  # Основная логика программы!
    menu_output()
    command = int(input(f"\nВведите команду: "))
    if command == 1:  # Список контактов
        con.display_a_list_of_contacts()
    elif command == 2:  # Добавить контакт
        clear_terminal()
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        phone = input("Телефон: ")
        con.add_contact_important(first_name, last_name, phone)
        # Ввод дополнительной информации
        clear_terminal()
        command_different = input("Ввести дополнительную информацию: ")
        if command_different == 'Да':
            pass
        elif command_different == 'Нет':
            pass
    elif command == 3:  # Изменить контакт
        clear_terminal()
        pass
    elif command == 4:  # Удалить контакт
        clear_terminal()
        pass
    elif command == 5:  # Закрыть программу
        clear_terminal()
        con.db.close_connection()
        exit()
    else:
        clear_terminal()
        print('Такой команды не существует!')


while True:
    programm_operation()
