import sqlite3

def reset_back_to_start():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS users")
    if a == "y" or a == "yes":
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (uid INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     age INTEGER NOT NULL
                     )''')

    conn.commit()

    c.close()
    conn.close()


def update_this(uid, name=None, email=None, age=None):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    update_fields = []
    update_values = []
    if name:
        update_fields.append("name = ?")
        update_values.append(name)
    if email:
        update_fields.append("email = ?")
        update_values.append(email)
    if age is not None:
        update_fields.append("age = ?")
        update_values.append(age)

    if len(update_fields) > 0:
        update_query = "UPDATE users SET " + ",".join(update_fields) + " WHERE uid = ?"
        update_values.append(uid)
        c.execute(update_query, tuple(update_values))
        conn.commit()
    conn.close()


def insert_this(name="", email="", age=0):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    c.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    uid = c.lastrowid
    conn.commit()

    c.close()
    conn.close()

    return uid


def read_for(uid=-1):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    if uid != -1:
        c.execute("SELECT * FROM users WHERE uid = ?", (uid,))
        result = str(c.fetchone())

    else:
        c.execute("SELECT * FROM users")
        result = c.fetchall()

    c.close()
    conn.close()

    return result
