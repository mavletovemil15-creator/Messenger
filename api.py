from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

router = APIRouter()


class User(BaseModel):
    username: str
    password: str


class Message(BaseModel):
    sender: str
    receiver: str
    message: str


@router.post("/register")
def register(user: User):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        conn.commit()

        return {
            "status": "ok",
            "message": "Пользователь зарегистрирован"
        }

    except sqlite3.IntegrityError:
        return {
            "status": "error",
            "message": "Такой пользователь уже существует"
        }

    finally:
        conn.close()


@router.post("/login")
def login(user: User):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (user.username, user.password)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return {
            "status": "ok",
            "message": "Вход выполнен"
        }

    else:
        return {
            "status": "error",
            "message": "Неверный логин или пароль"
        }


@router.post("/send_message")
def send_message(msg: Message):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)",
        (msg.sender, msg.receiver, msg.message)
    )

    conn.commit()
    conn.close()

    return {
        "status": "ok",
        "message": "Сообщение отправлено"
    }


@router.post("/get_messages")
def get_messages(user: Message):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sender, message
        FROM messages
        WHERE receiver=?
        """,
        (user.receiver,)
    )

    messages = cursor.fetchall()

    conn.close()

    return {
        "messages": messages
    }
