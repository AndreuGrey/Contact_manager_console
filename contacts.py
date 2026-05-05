# Управление контактами через Базу данных!
import database as db


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
    result = db.output_first_contacts()
    return result


# Нужно ещё сделать ввод доп.информации через проверку на созданность
def output_additionally(first_name, last_name, phone):
    result = db.check_create_contact(first_name, last_name, phone)
    if result:
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
