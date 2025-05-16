

from app.db.models import User , ChatHistory
from app.db.schemas import ChatRequest
from app.utils.gemini_client import generate_response

def get_or_create_user(db, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user



def process_chat(db, chat_data: ChatRequest):
    user = get_or_create_user(db, chat_data.username)

    response = generate_response(chat_data.message)

    chat = ChatHistory(
        user_id=user.id,
        prompt=chat_data.message,
        response=response
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)

    # ✅ Updated key to "answer"
    return {"answer": response}



