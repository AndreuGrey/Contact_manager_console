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


# Выводит список контактов
def output_ten_contacts(offset):
    try:
        cur.execute("""
            SELECT last_name, first_name, phone
            FROM contacts
            ORDER BY id
            LIMIT 10 OFFSET ?
        """, (offset,))

        display_result = cur.fetchall()
        if not display_result:
            print("На этой странице нет данных!")
            return False
        else:
            for i in display_result:
                print(*i)
            return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Проверка на созданность
def check_created_contact(first_name, last_name, phone):
    try:
        cur.execute("""
            SELECT 1
            FROM contacts
            WHERE first_name = ? AND last_name = ? AND phone = ?
        """, (first_name, last_name, phone))

        result_check = cur.fetchone()
        if result_check[0] == 1:
            return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


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
def change_of_contact(command_change, replacement_of_value, first_name, last_name):
    try:
        # Можно сделать список названия колонки и выборку, но пусть будет так
        match command_change:
            case 1:  # Фамилия
                cur.execute("""
                    UPDATE contacts
                    SET last_name = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case 2:  # Имя
                cur.execute("""
                    UPDATE contacts
                    SET first_name = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case 3:  # Отчество
                cur.execute("""
                    UPDATE contacts
                    SET middle_name = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case 4:  # Номер телефона
                cur.execute("""
                    UPDATE contacts
                    SET phone = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case 5:  # Электронная почта
                cur.execute("""
                    UPDATE contacts
                    SET email = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case 6:  # Дата рождения
                cur.execute("""
                    UPDATE contacts
                    SET birth_date = ?
                    WHERE first_name = ? AND last_name = ?
                """, (replacement_of_value, first_name, last_name))
            case _:  # else
                return False

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False


# Удаление контакта с базы данных ----
def delete_contact(first_name, last_name, phone):
    try:
        cur.execute("""
            DELETE FROM contacts
            WHERE first_name = ? AND last_name = ? AND phone = ?
        """, (first_name, last_name, phone))

        con.commit()
        return True

    except sql.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
