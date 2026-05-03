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


def display_a_list_of_contacts():  # Выводит список 10 контактов
    try:
        db.cur.execute("""
            SELECT *
            FROM contacts
            LIMIT 10
        """)

        display_result = db.cur.fetchall()
        for i in display_result:
            print(i)

    except db.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
