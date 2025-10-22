# models.py
# This file defines your database tables using SQLAlchemy ORM classes.

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# Define a "users" table
class User(Base):
    __tablename__ = "users"  # table name in database

    # Columns (fields)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
