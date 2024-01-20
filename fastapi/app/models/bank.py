from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy import func

from app.core.database import Base
from sqlalchemy.orm import relationship, mapped_column


class BankModel(Base):
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    type = Column(String(255), index=True, nullable=True)
    country = Column(String(255), index=True, nullable=True)
    state = Column(String(255), index=True, nullable=True)
    logo_link = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # users = relationship("UserModel", secondary="user_banks", back_populates="banks")
    # cards = relationship('CardModel', back_populates='bank')
    # expenses = relationship('ExpenseModel', back_populates='bank')


class UserBankModel(Base):
    __tablename__ = "user_banks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    bank_id = mapped_column(ForeignKey('banks.id'))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
