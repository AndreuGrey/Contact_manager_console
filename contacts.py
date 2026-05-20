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


# Нужно ещё сделать ввод доп.информации через проверку на созданность
def output_additionally():
    result_check = db.check_create_contact()
    if result_check:
        print("Такой контакт есть")


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
