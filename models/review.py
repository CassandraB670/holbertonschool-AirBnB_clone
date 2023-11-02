#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
     Represent a review
    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): text
    """

    place_id = str("")
    user_id = str("")
    text = str("")
