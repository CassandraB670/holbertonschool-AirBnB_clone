#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class testBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    def setUp(self):
        """Set up for the test"""
        self.model = BaseModel()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_string(self):
        """Test if 'id' is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test if 'created_at' is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if 'updated_at' is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_created_and_updated_at_are_equal_on_init(self):
        """Test if 'created_at' and 'updated_at' are equal on initialization"""
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str_representation(self):
        """Test the string representation"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method_updates_updated_at(self):
        """Test if the 'save' method updates 'updated_at'"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
