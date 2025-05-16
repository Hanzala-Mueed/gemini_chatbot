Introduction:

- Gemini Chatbot is an intelligent conversational assistant powered by Google's Gemini model.
- It allows users to interact naturally through a clean Streamlit frontend.
- All user prompts and AI responses are stored in a PostgreSQL database using SQLAlchemy.
- The backend is built with FastAPI, enabling fast and scalable API communication.
- This project demonstrates full-stack AI integration with persistent chat history and user management.


gemini_chatbot/
│
├── app/                          # FastAPI backend
│   ├── __init__.py
│   ├── main.py                   # FastAPI entry point
│   ├── api/                      # Route definitions
│   │   ├── __init__.py
│   │   └── chat.py               # /chat endpoint
│   ├── core/                     # Configuration, constants
│   │   ├── __init__.py
│   │   └── config.py             # ENV, Gemini key, DB URL
│   ├── db/                       # Database setup and models
│   │   ├── __init__.py
│   │   ├── database.py           # Engine, SessionLocal, Base
│   │   ├── models.py             # SQLAlchemy models
│   │   └── schemas.py            # Pydantic schemas
│   ├── services/                 # Business logic
│   │   ├── __init__.py
│   │   └── chat_service.py       # Prompt → Gemini → Save
│   └── utils/
│       └── gemini_client.py      # Gemini API wrapper
│
├── frontend/                     # Streamlit app
│   └── app.py                    # Streamlit UI logic
│
├── .env                          # ENV vars (DB URL, Gemini key)
├── requirements.txt              # Python dependencies
├── README.md
└── run.sh                        # Optional: bash script to run all
