import sqlite3


def connect_db():
    conn = sqlite3.connect("app.db")
    return conn


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_name TEXT,
        completed INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """
    )

    conn.commit()
    conn.close()


def add_user(username):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        print("Kullanıcı oluşturuldu.")
    except sqlite3.IntegrityError:
        print("Bu kullanıcı zaten var!")

    conn.close()


def add_task(user_id, task):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (user_id, task_name) VALUES (?, ?)", (user_id, task)
    )
    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, task_name, completed FROM tasks WHERE user_id = ?", (user_id,)
    )
    tasks = cursor.fetchall()

    conn.close()
    return tasks


def get_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    conn.close()
    return users


def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def complete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
