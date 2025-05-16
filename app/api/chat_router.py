from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.services.chat_service import process_chat

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/chat")
def chat(chat_data: schemas.ChatRequest, db: Session = Depends(get_db)):
    return process_chat(db, chat_data)
