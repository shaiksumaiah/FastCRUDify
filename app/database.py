# database.py
# This file sets up the database connection and session management.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite (stored in local file app.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Create a database engine
# check_same_thread=False is required only for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session maker (used to interact with the DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models (tables)
Base = declarative_base()
