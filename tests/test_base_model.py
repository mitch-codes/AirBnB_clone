#!/usr/bin/python3
import sys
sys.path.append('..')
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """class testing BaseModel class capabilities"""
        
    def test_save(self):
        base = BaseModel()
        oldTime = base.updated_at
        base.save()
        newTime = base.updated_at
        self.assertNotEqual(oldTime, newTime)
