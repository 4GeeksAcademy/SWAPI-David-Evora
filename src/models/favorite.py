from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db

class Favorite(db.Model):
    __tablename__ = "favorite"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    people_id: Mapped[int] = mapped_column(ForeignKey('people.id'), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicle.id'), nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=True)

    user: Mapped["User"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")
    vehicle: Mapped["Vehicle"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")

    def to_dict(self):
        return({
            "id": self.id,
            "user_id": self.user_id,
            "people": self.people.name if self.people else None,
            "planet": self.planet.name if self.planet else None,
            "vehicle": self.vehicle.name if self.vehicle else None
        })