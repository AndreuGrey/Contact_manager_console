# Управление контактами через Базу данных!
import database as db


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


# Выводит список 10 первых контактов
def output_first_contacts():
    result, check_list = db.output_first_contacts()
    return result, check_list


# Нужно ещё сделать ввод доп.информации через проверку на созданность
def output_additionally(check_list):
    result_check = db.check_create_contact(check_list)
    if result_check:
        print("Такой контакт есть")


# Выводит 10 следующих контактов


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
