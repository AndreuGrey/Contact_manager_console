# Основной файл для меню
import tests as test
import contacts as con


def clear_terminal():  # Очищает терминал в VS Code
    print("\033[H\033[J", end="")


def get_menu_choice() -> int | None:  # Вывод списка доступных команд
    menu_choice = [
        '1. Список контактов',
        '2. Добавить контакт',
        '3. Изменить контакт',
        '4. Удалить контакт',
        '5. Закрыть программу'
    ]

    clear_terminal()

    while True:
        print('\n'.join(menu_choice))

        input_user = input(f"\nВведите команду: ").strip()
        is_valid, error_message = test.command_input_test(input_user)

        clear_terminal()

        if is_valid:
            return int(input_user)
        else:
            print(
                f"Ошибка: {error_message}\n"
                "Попробуйте ввести снова!\n"
            )


def programm_operation(input_user: int):  # Выбор операции
    if input_user == 1:  # Список контактов
        clear_terminal()
        con.output_ten_contacts()
    elif input_user == 2:  # Добавить контакт
        clear_terminal()
        con.add_contact_important()
    elif input_user == 3:  # Изменить контакт
        clear_terminal()
        con.change_of_contact()
    elif input_user == 4:  # Удалить контакт
        clear_terminal()
        con.delete_contact()
    elif input_user == 5:  # Закрыть программу
        clear_terminal()
        con.close_connection()
        exit()
    else:
        clear_terminal()
        print('Такой команды не существует!')


while True:
    input_user = get_menu_choice()
    programm_operation(input_user)
