# deps.py
# This file defines dependencies like database session creation.

from .database import SessionLocal

# Dependency that creates a new DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db  # provide the session to the path operation
    finally:
        db.close()  # close the connection after request
