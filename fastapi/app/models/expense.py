from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from app.core.database import Base


class ExpenseModel(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    amount = Column(Float(10, asdecimal=True), nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)
    category_id = mapped_column(ForeignKey('categories.id'))
    payment_mode = Column(String(50), index=True, nullable=True, default=None)
    card_id = mapped_column(ForeignKey('cards.id'))
    bank_id = mapped_column(ForeignKey('banks.id'))
    receipt_image = Column(String(255), nullable=True, default=None)
    description = Column(String(255), nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # user = relationship("UserModel", back_populates="expenses")
    # category = relationship("CategoryModel", back_populates="expenses")
    # tags = relationship("TagModel", secondary="expense_tags", back_populates="expenses")
    # card = relationship("CardModel", back_populates="expenses")
    # bank = relationship("BankModel", back_populates="expenses")


class TagModel(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True, unique=True)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # expenses = relationship("ExpenseModel", secondary="expense_tags", back_populates="tags")


class ExpenseTag(Base):
    __tablename__ = "expense_tags"
    id = Column(Integer, primary_key=True, index=True)
    expense_id = mapped_column(ForeignKey('expenses.id'))
    tag_id = mapped_column(ForeignKey('tags.id'))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
