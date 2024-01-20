from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy import func

from app.core.database import Base
from sqlalchemy.orm import relationship, mapped_column


class CategoryModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    is_active = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # users = relationship("UserModel", secondary="user_categories", back_populates="categories")
    # expenses = relationship("ExpenseModel", back_populates="category")


class UserCategory(Base):
    __tablename__ = "user_categories"
    id = Column(Integer, primary_key=True, index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    category_id = mapped_column(ForeignKey('categories.id'))
    created_at = Column(DateTime, nullable=False, server_default=func.now())