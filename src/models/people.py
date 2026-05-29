from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from typing import List
from database import db

class People(db.Model):
    __tablename__ = "people"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    birth_year: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    eye_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    gender: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    hair_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    height: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    mass: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    skin_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    homeworld: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="people", cascade="all, delete-orphan")

    def to_dict(self):
        return({
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year or "Unknown",
            "created": self.created,
            "edited": self.edited,
        })