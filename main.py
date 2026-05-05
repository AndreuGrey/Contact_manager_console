# Основной файл для меню
import contacts as con


def clear_terminal():  # Очищает терминал в VS Code
    print("\033[H\033[J", end="")


def menu_output():  # Выводит список доступных команд
    menu_admin = [
        '1. Список контактов',
        '2. Добавить контакт',
        '3. Изменить контакт',
        '4. Удалить контакт',
        '5. Закрыть программу'
    ]

    for i in menu_admin:
        print(i)


def programm_operation():  # Основная логика программы!
    menu_output()
    command = int(input(f"\nВведите команду: "))
    if command == 1:  # Список контактов
        clear_terminal()
        result = con.output_first_contacts()
        if result:
            command_display = input(
                f"\nВывести дополнительную информацию? (Да/Нет): ")
            if command_display == 'Да':
                # Ошибка выборки данных (NameError)
                con.output_additionally(first_name, last_name, phone)
            elif command_display == 'Нет':
                clear_terminal()
                pass
            command_display = input(f"\nВывести ещё 10 контактов (Да/Нет): ")
            if command_display == 'Да':
                clear_terminal()
                pass
            elif command_display == 'Нет':
                clear_terminal()
                # Нужно закрыть список? ----
                pass
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
            elif command_different == 'Нет':
                pass
    elif command == 3:  # Изменить контакт
        clear_terminal()
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
            # Удалить ли ещё контакт?
            pass
    elif command == 5:  # Закрыть программу
        clear_terminal()
        con.close_connection()
        exit()
    else:
        clear_terminal()
        print('Такой команды не существует!')


while True:
    programm_operation()
