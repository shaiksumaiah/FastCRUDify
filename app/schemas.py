# schemas.py
# This file defines Pydantic models for data validation and API schemas.

from pydantic import BaseModel

# Common fields for all user schemas
class UserBase(BaseModel):
    name: str
    email: str

# Used when creating a new user
class UserCreate(UserBase):
    pass

# Used when updating user data
class UserUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

# Used when returning user data (includes ID and is_active)
class UserRead(UserBase):
    id: int
    is_active: bool

    # orm_mode allows Pydantic to read SQLAlchemy objects directly
    class Config:
        orm_mode = True
