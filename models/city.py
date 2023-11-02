#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a City
    Attributes:
        name  (str): name of the city
        state_id (str): State.id
    """

    name = str("")
    state_id = str("")
