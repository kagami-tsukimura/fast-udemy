from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    url = Column(String(255), nullable=True)
    gender = Column(Integer, nullable=False)
    message = Column(String(200), nullable=False)
    is_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, name, email, url, gender, message, is_enabled):
        self.name = name
        self.email = email
        self.url = url
        self.gender = gender
        self.message = message
        self.is_enabled = is_enabled
        self.created_at = datetime.now()
