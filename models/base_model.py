#!/usr/bin/python3
"""Write the first class Base"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialization of the BaseModel Class
        Args:
            args: set of arguments
            kwargs: set of arguments with keyword
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """print representation str of the BaseModel Class
        Returns:
            str: string representation of instance
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the public instance attribute updated_at
        with current datetime
        updated_at : with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """returns a dictionary
        Return:
            dict: instance dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
