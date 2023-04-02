from fastapi import FastAPI
import requests
import sqlite3

# Створення баз даних
db = sqlite3.connect("users.db")
dbcomments = sqlite3.connect("comments.db")

# Створення курсора
cursor = db.cursor()
cursor_comments = dbcomments.cursor()

# Перевіряєм чи існує база даних. Якщо її не існує - то свторюємо її
try:
    file = open('users.db')
except IOError as e:
    cursor.execute("""
        CREATE TABLE users (
            id integer,
            name text,
            email text,
            gender text,
            status text
        )
    """)

try:
    file = open('comments.db')
except IOError as e:
    cursor_comments.execute("""
        CREATE TABLE comments (
            id integer,
            post_id integer,
            name text,
            email text,
            body text
        )
    """)

# Оновлення бази даних
db.commit()
dbcomments.commit()

urlTest = "https://gorest.co.in/public/v2/users"
responseTest = requests.get(urlTest)

cursor.execute("SELECT rowId FROM users")
# Перевіряєм чи пуста база даних users.db. І якщо вона пуста то записуєм туди данні
if cursor.fetchone() is None:
    # Цикл який перебирає всі дані які були отримані з сервера
    for user in responseTest.json():
        id = int(user["id"])
        name = user["name"]
        email = user["email"]
        gender = user["gender"]
        status = user["status"]
        # Запис отриманих даних в локальну базу даних
        cursor.execute('''INSERT INTO users(id, name, email, gender, status)
                            VALUES(:id, :name, :email, :gender, :status)''',
                        {'id': id, 'name': name, 'email': email, 'gender': gender, 'status': status})

url_comments = "https://gorest.co.in/public/v2/comments"
response_comments = requests.get(url_comments)
cursor.execute("SELECT rowId FROM comments")
# Перевіряєм чи пуста база даних comments.db. І якщо вона пуста то записуєм туди данні
if cursor_comments.fetchone() is None:
    # Цикл який перебирає всі дані які були отримані з сервера
    for comment in response_comments.json():
        id = int(comment["id"])
        post_id = int(comment["post_id"])
        name = comment["name"]
        email = comment["email"]
        body = comment["body"]
        # Запис отриманих даних в локальну базу даних
        cursor.execute('''INSERT INTO comments(id, post_id, name, email, body)
                            VALUES(:id, :post_id, :name, :email, :body)''',
                        {'id': id, 'post_id': post_id, 'name': name, 'email': email, 'body': body})

# Створює змінну яка являється екземпляром FastAPI
app = FastAPI()

# Хендлер, который асинхронно запросит данные из БД о всех пользователях.
@app.get('/public/local/users/')
async def get_users():
    cursor.execute("SELECT * FROM users")
    return (cursor.fetchall())

# Хендлер, который асинхронно запросит данные о пользователе с конкретным ID
@app.get('/public/v2/user/{user_id}')
async def get_user(user_id: int):
    results = requests.get("https://gorest.co.in/public/v2/users/" + str(user_id))
    return (results.json())

# Хендлер, который асинхронно запросит данные из БД о всех сообщениях пользователя с конкретным ID.
@app.get('/public/v2/posts/{user_id}/comments')
async def get_user(user_id: int):
    cursor.execute("SELECT body FROM comments WHERE id =" + str(user_id))
    return (cursor.fetchall())