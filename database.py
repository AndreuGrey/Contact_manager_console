# Выполнение запросов и обновлений по БД!
import sqlite3 as sql


con = sql.connect("Contacts_database.db")
cur = con.cursor()


# Создаёт базу данных
def create_db():
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


# Проверяет существование таблицы
def check_table():
    try:
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='contacts'
        """)

        result = cur.fetchall()  # Нужно проверить есть ли строки вообще
        if result[0][0] != 'contacts':
            create_db()

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()


# Удаляет базу данных (Администрация)
def drop_table_db():
    try:
        cur.execute("DROP TABLE IF EXISTS contacts")

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        con.rollback()
        return False


# Закрывает соединение с базой данных
def close_connection():
    try:
        cur.close()
        con.close()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Выводит список 10 первых контактов
def output_first_contacts():
    try:
        # Вывести те строки, значения которых не равно NULL
        cur.execute("""
            SELECT last_name, first_name, phone
            FROM contacts
            LIMIT 10
        """)

        display_result = cur.fetchall()
        # Нужно вывести красиво, не через массив
        for i in display_result:
            print(i)
        return True, display_result  # Выводит массив для сравнения

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Проверка на созданность
def check_create_contact(check_list):
    try:
        # Нужно написать запрос сравнения ----
        cur.execute("""
            ...
        """)

        check_result = cur.fetchall()
        return check_result

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Выводит следующие 10 контактов
def output_next_contacts():
    pass
    # Нужна проверка на rowid, чтобы вывести именно следующие


# Добавляет контакт с важной информацией
def add_contact_important(first_name, last_name, phone):
    try:
        cur.execute("""
            INSERT INTO contacts (id, first_name, last_name, phone)
            VALUES (MAX(id) + 1, ?, ?, ?)
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
                email = ?,
                birth_date = ?
            WHERE first_name = ? AND last_name = ?
        """, (middle_name, email, birth_date, first_name, last_name))

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Изменение контакта ----
def change_of_contacts():
    pass


# Удаление контакта с базы данных
def delete_contact(first_name, last_name, phone):
    try:
        # Удаление строки из таблицы
        cur.execute("""
            DELETE FROM contacts
            WHERE first_name = ? AND last_name = ? AND phone = ?
        """, (first_name, last_name, phone))

        # Дальше пересоздаём таблицу для выравнивания rowid

        # Создаём копирующую таблицу
        cur.execute("""
            CREATE TABLE copy_contacts AS
                    SELECT * FROM contacts
        """)

        # Очищаем исходную таблицу
        cur.execute("DELETE FROM contacts")

        # Сбрасываем автоинкремент
        cur.execute("""
            UPDATE sqlite_sequence 
            SET seq = 0
            WHERE name = contacts 
        """)

        # Вставляет данные обратно из copy_contacts
        cur.execute("""
            INSERT INTO contacts
            SELECT * FROM copy_contacts
        """)

        # Удаляем copy_contacts
        cur.execute("DROP TABLE IF EXISTS copy_contacts")

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
