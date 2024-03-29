#!/usr/bin/env python
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime


class BaseModel:

    """Base class for all models."""
    def __init__(self, *args, **kwargs):

        """
        Initialize the BaseModel class.
        Args:
            *args: unused arguments.
            **kwargs: key/value dictionary
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime.
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values
            of __dict__ of the instance.
        """

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__

        return dict_copy

    def __str__(self):
        """
            Return a string representation of the BaseModel class.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
