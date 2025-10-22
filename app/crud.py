# crud.py
# This file contains functions that perform actual DB operations (Create, Read, Update, Delete).

from sqlalchemy.orm import Session
from . import models, schemas

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)        # add user to session
    db.commit()            # save to database
    db.refresh(db_user)    # refresh object with DB data
    return db_user

# Get all users
def get_users(db: Session):
    return db.query(models.User).all()

# Get a single user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Update user details
def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        if user_update.name is not None:
            user.name = user_update.name
        if user_update.is_active is not None:
            user.is_active = user_update.is_active
        db.commit()
        db.refresh(user)
    return user

# Delete a user
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
