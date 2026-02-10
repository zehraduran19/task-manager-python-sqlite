# 🗂️ User & Task Management System (Python + SQLite)

This project is a simple **Command Line Interface (CLI)** application built with **Python** and **SQLite**.  
It allows users to create accounts and manage their tasks with a database-supported system.

The goal of this project is to practice working with **databases** in Python and to build a real-life mini system.

---

## 🚀 Features

✅ Create users  
✅ List users  
✅ Add tasks for a user  
✅ List tasks of a user  
✅ Delete tasks  
✅ Mark tasks as completed (✅ / ❌)  
✅ Data is stored permanently using SQLite database (`app.db`)

---

## 🛠️ Technologies Used

- Python
- SQLite3 (built-in Python database library)

---

## 📂 Project Structure

project/
│
├── main.py
├── database.py
├── app.db
└── README.md



---

## ▶️ How to Run

1. Open the project folder in VS Code  
2. Open terminal and run:

```bash
python main.py


📌 Menu Options
1 - Create user
2 - Add task
3 - List tasks
4 - List users
5 - Delete task
6 - Complete task
7 - Exit

💡 Example Output
1 - Create user
2 - Add task
3 - List tasks
4 - List users
5 - Delete task
6 - Complete task
7 - Exit

Choice: 1
Username: zehra
User created successfully.

Choice: 2
User ID: 1
Task: Study Python
Task added.

Choice: 3
User ID: 1
ID: 1 - Study Python ❌

🎯 What I Learned

In this project, I learned how to:

create and manage SQLite database tables

connect Python to a database using sqlite3

store data permanently

build a CLI-based mini backend system

use CRUD operations (Create, Read, Update, Delete)

👩‍💻 Author

Zehra Duran


---
