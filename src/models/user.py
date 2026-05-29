from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from typing import List
from database import db

class User(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    username: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    created: Mapped[datetime] = mapped_column(DateTime,default=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):
        return({
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created": self.created,
            "favorites": [fav.to_dict() for fav in self.favorites]
        })