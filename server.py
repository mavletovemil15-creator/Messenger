from fastapi import FastAPI
import uvicorn

from database import create_tables
from api import router

app = FastAPI()

create_tables()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Messenger Server работает!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)