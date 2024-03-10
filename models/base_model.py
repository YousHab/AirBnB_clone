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

    def __str__(self):
        """
            Return a string representation of the BaseModel class.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime.
        """
        self.updated_at = datetime.today()

    def to_dic(self):
        """
            Returns a dictionary containing all keys/values
            of __dict__ of the instance.
        """
        return self.__dict__
