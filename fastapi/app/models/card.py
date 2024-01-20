from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime
from sqlalchemy import func, ForeignKey

from app.core.database import Base


class CardModel(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    bank_id = mapped_column(ForeignKey('banks.id'))
    card_number = Column(String(20))
    exp_month = Column(Integer)
    exp_year = Column(Integer)
    cvv = Column(Integer)
    type = Column(String(255), index=True)
    is_active = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # expenses = relationship("ExpenseModel", back_populates='card')
    # bank = relationship("BankModel", back_populates='cards')
    # user = relationship("UserModel", back_populates='cards')
