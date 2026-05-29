from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from typing import List
from database import db

class Vehicle(db.Model):
    __tablename__ = "vehicle"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    model: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    vehicle_class: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    speed: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    weight: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    length: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="vehicle", cascade="all, delete-orphan")
