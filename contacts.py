# Файл для управления запросами в самой программе
import sqlite3 as sql


con = sql.connect("Contacts_database.db")
cur = con.cursor()


def add_contact_important(first_name, last_name, phone):
    try:
        cur.execute("""
            INSERT INTO contacts (first_name, last_name, phone)
            VALUES (?, ?, ?)
        """, (first_name, last_name, phone))

        con.commit()
        print('Новый контакт успешно добавлен в Контакты!')
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()
        return False


def add_contact_different(first_name, middle_name, last_name, email, birth_date):
    try:
        cur.execute("""
            INSERT INTO contacts (middle_name, email, birth_date)
            VALUES (?, ?, ?)
        """, (middle_name, email, birth_date))

        con.commit()
        print(f"Информация по контакту {last_name, first_name} обновлена!")
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
