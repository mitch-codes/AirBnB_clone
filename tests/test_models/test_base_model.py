#!/usr/bin/python3
"""
Test suits for the base model
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def setUp(self):
        """
        Classes needed for testing
        """
        pass

    def test_save(self):
        base = BaseModel()
        oldTime = base.updated_at
        base.save()
        newTime = base.updated_at
        self.assertNotEqual(oldTime, newTime)

    def test_basic(self):
        """
        Tests basic imputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])
    def test_to_dict(self):
        """test if to_dict returns right dict"""
        base = BaseModel()
        my_dict = base.to_dict()
        self.assertEqual(base.id, my_dict["id"])

    def test_str(self):
        """assert that str function is correct"""
        base = BaseModel()
        base.name = "mimi"
        my_dict = str(base)
        self.assertIn("'name': 'mimi'", my_dict)

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass
    
    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass


if __name__ == '__main__':
    unittest.main()
