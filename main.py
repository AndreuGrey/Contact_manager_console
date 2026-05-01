# Основной файл для меню
import contacts as ct
import database as db


def check_table():
    db.cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='contacts'
    """)

    result = db.cur.fetchall()
    if result[0][0] == 'contacts':
        menu_output()
    else:
        db.create_db()


def menu_output():
    menu = [
        '1. Список контактов',
        '2. Добавить контакт',
        '3. Изменить контакт',
        '4. Удалить контакт'
    ]

    for i in menu:
        print(i)


check_table()
