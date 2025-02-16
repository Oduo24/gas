#!/usr/bin/python3
"""Base model module. To be inherited by all the models"""

from sqlalchemy import Column, String, DateTime
from datetime import datetime
import pytz
import uuid


class BaseModel:
    """Defines the base class to be inherited by other models"""
    id = Column(String(100), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(pytz.utc))

    def __init__(self, *args, **kwargs):
        """This is the class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(pytz.utc)


    



