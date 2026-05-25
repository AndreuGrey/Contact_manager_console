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

    clear_terminal()
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
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        phone = input("Телефон: ")
        result = con.add_contact_important(first_name, last_name, phone)
        if result:
            # Ввод дополнительной информации после добавления
            clear_terminal()
            command_different = input(
                f"\nВвести дополнительную информацию (Да/Нет): ")
            if command_different == 'Да':
                middle_name = input("Отчество: ")
                email = input("Электронная почта: ")
                birth_date = input("Дата рождения: ")
                con.add_contact_different(
                    first_name, middle_name, last_name, email, birth_date)
                clear_terminal()
            elif command_different == 'Нет':
                pass
    elif command == 3:  # Изменить контакт
        clear_terminal()
        # Изменение существующего контакта
        # Ввод дополнительной информации при существующем контакте
        pass
    elif command == 4:  # Удалить контакт
        clear_terminal()
        print("Какой контакт удалить?")
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        phone = input("Телефон: ")
        result = con.delete_contact(first_name, last_name, phone)
        if result:
            while True:
                command_delete = input("Удалить ещё контакт? (Да/Нет): ")
                if command_delete.lower() == 'да':
                    clear_terminal()
                    print("Какой контакт удалить?")
                    first_name = input("Имя: ")
                    last_name = input("Фамилия: ")
                    phone = input("Телефон: ")
                    con.delete_contact(first_name, last_name, phone)
                    return True
                elif command_delete.lower() == 'нет':
                    clear_terminal()
                    return False
    elif command == 5:  # Закрыть программу
        clear_terminal()
        con.close_connection()
        exit()
    else:
        clear_terminal()
        print('Такой команды не существует!')


while True:
    programm_operation()
