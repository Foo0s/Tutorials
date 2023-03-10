import sqlite3
from register_apps.apps import Application_register


#Подключение БД.
conn = sqlite3.connect("base_data.db")
#Создание объекта - курсора. - делает sql-запросы.
cursor = conn.cursor()

#Создание таблиц.
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT,
        time TEXT);
""")
conn.commit() #Сохранение изменений.

#Добавление данных в таблицу.
def update_data(str1, str2, str3):
    user = (str1, str2, str3)
    cursor.execute(f"INSERT INTO users(email, password, time) VALUES(?, ?, ?);", user)
    conn.commit() #Сохранение изменений

def check_users(str1, str2, str3):
    cursor.execute(f"SELECT email FROM users WHERE email=?", (str1,))
    if not cursor.fetchall():
        update_data(str(str1), str(str2), str(str3))
    else:
        Application_register.answer_user(True)
def reg_users(str1, str2, str3):
    cursor.execute(f"SELECT email, password FROM users WHERE email=? AND password=?", (str1, str2))
    if not cursor.fetchall():
        Application_register.answer_mistake_for_user(True)
    else:
        Application_register.hello_user(True)