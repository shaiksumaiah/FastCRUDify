# FastCRUDify 🚀

**FastCRUDify** is a full-featured **User CRUD API** built with **FastAPI** and **SQLAlchemy**.  
This project allows you to **Create, Read, Update, and Delete users** easily, and demonstrates best practices for building RESTful APIs with Python.

---

## Features ✨
- ✅ Create, Read, Update, Delete (CRUD) operations for users
- ✅ Data validation with **Pydantic**
- ✅ Database integration using **SQLAlchemy**
- ✅ Modular project structure with routers and schemas
- ✅ Automatic API documentation with **Swagger UI** and **ReDoc**
- ✅ Environment variables support via **python-dotenv**

---

## Tech Stack 🛠️
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn (ASGI server)
- SQLite (default, can be switched to PostgreSQL/MySQL)

---

## Project Structure 📁

fastapi_sumaiah_user_crud/
│
├─ app/
│ ├─ main.py # Application entry point
│ ├─ database.py # Database connection setup
│ ├─ models.py # SQLAlchemy models
│ ├─ schemas.py # Pydantic schemas
│ ├─ crud.py # CRUD helper functions
│ ├─ deps.py # Dependency injections
│ └─ routers/
│ └─ users.py # User endpoints
│
├─ .gitignore # Git ignore rules
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation

yaml
Copy code

---

## Installation ⚡

1. **Clone the repo**
```bash
git clone https://github.com/shaiksumaiah/FastCRUDify.git
cd FastCRUDify
Create a virtual environment

bash
Copy code
python -m venv .venv
source .venv/Scripts/activate   # Windows
# OR
source .venv/bin/activate      # macOS/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the server

bash
Copy code
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Usage 📝
Use Swagger UI or any API client (Postman, Insomnia) to test the endpoints.

All endpoints are prefixed under /users.

Supports JSON input/output.

Contribution 🤝
Feel free to contribute to FastCRUDify!

Fork the repository

Create a branch (git checkout -b feature/new-feature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/new-feature)

Create a Pull Request

License 📄
This project is open-source and available under the MIT License.

Author ✨
Shaik Sumaiah
GitHub: https://github.com/shaiksumaiah

yaml
Copy code

---

If you want, I can also **create a `.gitignore` for you** specifically for this FastAPI + Python project, so you won’t push unnecessary files like `.pyc` or `.venv`.  

Do you want me to do that next?






