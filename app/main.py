from fastapi import FastAPI
from app.api import chat_router
from app.db import database, models

app = FastAPI()


models.Base.metadata.create_all(bind=database.engine)


app.include_router(chat_router.router)
