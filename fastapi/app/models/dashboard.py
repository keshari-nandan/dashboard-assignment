from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date, ForeignKey, JSON
from datetime import datetime
from sqlalchemy import func

from app.core.database import Base
from sqlalchemy.orm import relationship, mapped_column


class DashboardModel(Base):
    __tablename__ = "dashboards"
    id = Column(Integer, primary_key=True, index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    name = Column(String(255), index=True)
    default = Column(Boolean, nullable=False, default=False)
    config = Column(JSON, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # user = relationship("UserModel", back_populates="dashboards")