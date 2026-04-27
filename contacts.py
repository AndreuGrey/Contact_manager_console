# Файл для управления запросами в самой программе
import sqlite3 as sql


con = sql.connect("Contacts_database.db")
cur = con.cursor()


def add_contact_in_database():
    try:
        cur.execute("""
            INSERT INTO contacts
            VALUES ...
        """)

        con.commit()

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()

    finally:
        print('Новый контакт успешно добавлен в БД!')
