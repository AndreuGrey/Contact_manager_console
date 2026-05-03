# Выполнение запросов и обновлений по БД!
import sqlite3 as sql


con = sql.connect("Contacts_database.db")
cur = con.cursor()


def create_db():  # Создаёт базу данных
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
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
        print('База данных успешно создана!')

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()


def check_table():  # Проверяет существование таблицы
    try:
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='contacts'
        """)

        result = cur.fetchall()
        if result[0][0] != 'contacts':
            create_db()

    # Не знаю что вывести в роли ошибки!
    except ValueError():
        pass


def drop_table_db():  # Удаляет базу данных
    try:
        cur.execute("DROP TABLE IF EXISTS contacts")

        con.commit()
        print('База данных успешно удалена!')

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()


def close_connection():  # Закрывает соединение с базой данных
    try:
        cur.close()
        con.close()

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")

    finally:
        print('Соединение успешно закрыто!')
