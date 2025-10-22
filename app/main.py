# main.py
# This is the main entry point of your FastAPI application.

from fastapi import FastAPI
from .database import Base, engine
from .routers import users

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(title="User CRUD API using FastAPI and SQLAlchemy")

# Include the user router (connect endpoints)
app.include_router(users.router)

# Root endpoint for testing
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI User CRUD Application!"}
