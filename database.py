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

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()


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


# Добавляет контакт с важной информацией
def add_contact_important(first_name, last_name, phone):
    try:
        cur.execute("""
            INSERT INTO contacts (first_name, last_name, phone)
            VALUES (?, ?, ?)
        """, (first_name, last_name, phone))

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()
        return False


# Добавляет дополнительную информацию к созданному контакту
def add_contact_different(first_name, middle_name, last_name, email, birth_date):
    try:
        cur.execute("""
            UPDATE contacts
            SET middle_name = ?,
            SET email = ?,
            SET birth_date = ?
            WHERE first_name = ? AND last_name = ?
        """, (middle_name, email, birth_date, first_name, last_name))

        con.commit()
        print(f"Информация по контакту {last_name, first_name} обновлена!")
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
