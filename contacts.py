# Управление контактами через Базу данных!
import database as db


def clear_terminal():  # Очищает терминал в VS Code
    print("\033[H\033[J", end="")


def menu_output():  # Список команд вывода
    menu_output = [
        '1.Предыдущая страница',
        '2.Следующая страница'
    ]

    for i in menu_output:
        print(f"{i}")


def menu_check():  # Список для проверки
    pass


def menu_change():  # Список для изменения
    menu_change = [
        '1. Фамилия',
        '2. Имя',
        '3. Отчество',
        '4. Номер телефона',
        '5. Электронная почта',
        '6. Дата рождения'
    ]

    clear_terminal()

    for i in menu_change:
        print(f"{i}")


# Удаление таблицы (Администрация)
def drop_table_db():
    result = db.drop_table_db()
    if result:
        print("База данных успешно удалена!")


# Добавляет контакт с важной информацией
def add_contact_important(first_name, last_name, phone):
    result = db.add_contact_important(first_name, last_name, phone)
    if result:
        print(f"{last_name} {first_name} успешно добавлен в Контакты!")
    return result


# Добавляет дополнительную информацию к созданному контакту
def add_contact_different(first_name, middle_name, last_name, email, birth_date):
    result = db.add_contact_different(
        first_name, middle_name, last_name, email, birth_date)
    if result:
        print(f"Информация по {last_name} {first_name} обновлена!")
    return result


# Выводит список по 10 контактов
def output_ten_contacts():
    offset = 0
    pages = 1
    result = db.output_ten_contacts(offset)
    print(f"\nСтраница: {pages}")
    while result == True:
        if pages == 1:
            command_output = input(f"\nВывести следующую страницу(Да/Нет): ")
            if command_output.lower() == 'да':
                pages += 1
                clear_terminal()
                offset += 10
                result = db.output_ten_contacts(offset)
                print(f"\nСтраница: {pages}")
            else:
                clear_terminal()
                break
        if pages > 1:
            menu_output()
            command_output = int(input(f"\nВведите команду: "))
            if command_output == 1 and pages > 1:
                pages -= 1
                clear_terminal()
                offset -= 10
                result = db.output_ten_contacts(offset)
                print(f"\nСтраница: {pages}")
            elif command_output == 2 and pages > 1:
                pages += 1
                clear_terminal()
                offset += 10
                result = db.output_ten_contacts(offset)
                print(f"\nСтраница: {pages}")
            else:
                clear_terminal()
                break


# Проверка на созданность контакта
def check_created_contact(first_name, last_name, phone):
    # Можно добавить выбор по чем проверять ----
    result_check = db.check_created_contact(first_name, last_name, phone)
    if result_check:
        return True
    else:
        print("Такого контакта нет!")
        return False


# Изменить контактные данные
def change_of_contact():
    # Нужно изменить проверку
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    phone = input("Телефон: ")
    result_check = check_created_contact(first_name, last_name, phone)
    if result_check:
        menu_change()
        command_change = int(input(f"\nЧто нужно изменить: "))
        match command_change:  # Впервые пробую метод match case
            case 1:  # Фамилия
                clear_terminal()
                replacement_of_value = input("Новая фамалия: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Фамилия успешно изменена!")
                else:
                    print("Ошибка в изменении")
            case 2:  # Имя
                clear_terminal()
                replacement_of_value = input("Новое имя: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Фамилия успешно изменена!")
                else:
                    print("Ошибка в изменении")
            case 3:  # Отчество
                clear_terminal()
                replacement_of_value = input("Новое отчество: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Отчество успешно изменено!")
                else:
                    print("Ошибка в изменении")
            case 4:  # Номер телефона
                clear_terminal()
                replacement_of_value = input("Новый телефон: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Номер телефона успешно изменён!")
                else:
                    print("Ошибка в изменении")
            case 5:  # Электронная почта
                clear_terminal()
                replacement_of_value = input("Новая электронная почта: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Электронная почта успешно изменена!")
                else:
                    print("Ошибка в изменении")
            case 6:  # Дата рождения
                clear_terminal()
                replacement_of_value = input("Новая дата рождения: ")
                result_change = db.change_of_contact(
                    command_change, replacement_of_value, first_name, last_name)
                if result_change:
                    print("Дата рождения успешно изменена!")
                else:
                    print("Ошибка в изменении")
            case _:
                print("Неизвестный статус!")


# Удаление контакта с базы данных
def delete_contact(first_name, last_name, phone):
    result = db.delete_contact(first_name, last_name, phone)
    if result:
        print(f"Контакт {last_name} {first_name} удалён!")
        return result


# Закрывает соединение с базой данных
def close_connection():
    result = db.close_connection()
    if result:
        print("Соединение с БД закрыто!")
