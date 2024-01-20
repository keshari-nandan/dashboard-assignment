from app.models.card import *
from app.models.bank import *
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from datetime import datetime

from starlette.authentication import SimpleUser

from app.core.database import Base

from sqlalchemy.orm import relationship, mapped_column


class RequestUser(SimpleUser):
    def __init__(self, id, username, name):
        self.id = id
        self.username = username
        self.name = name
        super().__init__(self.username)


class UserModel(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    is_demo = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # expenses = relationship("ExpenseModel", back_populates="user")
    # banks = relationship("BankModel", secondary="user_banks", back_populates="users")
    # cards = relationship("CardModel", back_populates="user")
    # dashboards = relationship("DashboardModel", back_populates="user")
    # categories = relationship("CategoryModel", secondary="user_categories", back_populates="users")
