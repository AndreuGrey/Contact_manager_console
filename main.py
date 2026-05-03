# Основной файл для меню
import contacts as ct


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
        ct.display_a_list_of_contacts()
    elif command == 2:  # Добавить контакт
        pass
    elif command == 3:  # Изменить контакт
        pass
    elif command == 4:  # Удалить контакт
        pass
    elif command == 5:  # Закрыть программу
        ct.db.close_connection()
        exit()
    else:
        print('Такой команды не существует!')


while True:
    programm_operation()
