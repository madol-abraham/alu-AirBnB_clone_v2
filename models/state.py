#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete")

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute that returns a list of City instances"""
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

