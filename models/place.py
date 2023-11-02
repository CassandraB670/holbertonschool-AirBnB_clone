#!/usr/bin/python3
"""Defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represent a Place
    Attributes:
        city_id (str): City.id
        user_id (str): User.id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms into the place
        number_bathrooms (int): number of bathrooms into the place
        max_guest (int): number of guest
        price_by_night (int): price
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list of str): Amenity.id
    """

    city_id = str("")
    user_id = str("")
    name = str("")
    description = str("")
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
