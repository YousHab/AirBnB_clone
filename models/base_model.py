#!/usr/bin/env python
"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """Base class for all models."""
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class.
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

        else:
            pass
