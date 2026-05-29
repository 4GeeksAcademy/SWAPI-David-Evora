from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from typing import List
from database import db

class Planet(db.Model):
    __tablename__ = "planet"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    gravity: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    population: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    climate: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    terrain: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="planet", cascade="all, delete-orphan")

    def to_dict(self):
        return({
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity or "Unknown",
            "population": self.population or "Unknown",
            "created": self.created,
            "edited": self.edited,
        })