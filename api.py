from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

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
        return {"status": "ok", "message": "Пользователь зарегистрирован"}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "Такой пользователь уже существует"}
    finally:
        conn.close()