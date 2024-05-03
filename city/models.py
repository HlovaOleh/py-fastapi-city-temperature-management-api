from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from temperature.models import Temperature


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, unique=True)
    additional_info = Column(String(511), nullable=True)

    temperatures = relationship(Temperature, back_populates="city")