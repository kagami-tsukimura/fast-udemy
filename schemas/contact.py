from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Contact(BaseModel):
    id: int
    name: str
    email: str
    url: str
    gender: int
    message: str
    is_enabled: bool
    created_at: datetime
