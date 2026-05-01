# Файл для управления запросами в самой программе
import database as db


# Добавляет контакт с важной информацией
def add_contact_important(first_name, last_name, phone):
    try:
        db.cur.execute("""
            INSERT INTO contacts (first_name, last_name, phone)
            VALUES (?, ?, ?)
        """, (first_name, last_name, phone))

        db.con.commit()
        print('Новый контакт успешно добавлен в Контакты!')
        return True

    except db.Error as e:
        print(f"Ошибка базы данных: {e}")
        db.con.rollback()
        return False


# Добавляет информацию к созданному контакту
def add_contact_different(first_name, middle_name, last_name, email, birth_date):
    try:
        db.cur.execute("""
            INSERT INTO contacts (middle_name, email, birth_date)
            VALUES (?, ?, ?)
        """, (middle_name, email, birth_date))

        db.con.commit()
        print(f"Информация по контакту {last_name, first_name} обновлена!")
        return True

    except db.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
