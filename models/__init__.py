#!/usr/bin/python3
"""This module conect with the database, or object of class FileStorage
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
