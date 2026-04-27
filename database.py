# Создание и удаление базы данных!
import sqlite3 as sql


con = sql.connect("Contacts_database.db")
cur = con.cursor()


def create_db():  # Создаёт базу данных
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT,
            birth_date TEXT
            )
        """)

        con.commit()

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()

    finally:
        print('База данных успешно создана!')


def drop_db():  # Удаляет базу данных
    try:
        cur.execute("DROP TABLE IF EXISTS contacts")

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()

    finally:
        print('База данных успено удалена!')
