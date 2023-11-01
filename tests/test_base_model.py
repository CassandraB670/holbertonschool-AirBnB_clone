#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelInitialization(unittest.TestCase):
    """Tests related to BaseModel initialization"""

    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_created_and_updated_at_are_equal_on_init(self):
        self.assertEqual(self.model.created_at, self.model.updated_at)

class TestBaseModelStringRepresentation(unittest.TestCase):
    """Tests related to BaseModel string representation"""

    def setUp(self):
        self.model = BaseModel()

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_str(self):
        model_str = str(self.model)
        self.assertIsInstance(model_str, str)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn('id', model_str)
        self.assertIn(str(self.model.id), model_str)
        self.assertIn(str(self.model.__dict__), model_str)

class TestBaseModelSerialization(unittest.TestCase):
    """Tests related to BaseModel serialization"""

    def setUp(self):
        self.model = BaseModel()

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_method_includes_id(self):
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)

    def test_to_dict_method_includes_class_key(self):
        model_dict = self.model.to_dict()
        self.assertIn('__class__', model_dict)

class TestBaseModelMiscellaneous(unittest.TestCase):
    """Miscellaneous tests related to BaseModel"""

    def setUp(self):
        self.model = BaseModel()

    def test_save_method_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_id_unique_for_each_instance(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_and_updated_at_format(self):
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(self.model.created_at.strftime(iso_format), self.model.created_at.isoformat())
        self.assertEqual(self.model.updated_at.strftime(iso_format), self.model.updated_at.isoformat())

    def test_init_with_kwargs_removes_class_key(self):
        kwargs = {"__class__": "SomeClass", "name": "TestObject"}
        model = BaseModel(**kwargs)
        self.assertNotIn('__class__', model.__dict__)

    def test_init_with_kwargs_sets_attributes_correctly(self):
        kwargs = {"name": "TestObject", "created_at": "2023-01-01T00:00:00.123456", "value": 42}
        model = BaseModel(**kwargs)
        self.assertEqual(model.name, "TestObject")
        self.assertEqual(model.value, 42)
        self.assertIsInstance(model.created_at, datetime)
        self.assertEqual(model.created_at.isoformat(), "2023-01-01T00:00:00.123456")

    def test_init_with_datetime_format(self):
        kwargs = {"created_at": "2023-01-01T00:00:00.123456", "updated_at": "2023-02-02T01:01:01.654321"}
        model = BaseModel(**kwargs)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at.isoformat(), "2023-01-01T00:00:00.123456")
        self.assertEqual(model.updated_at.isoformat(), "2023-02-02T01:01:01.654321")

    def test_init_with_id(self):
        custom_id = "custom_id"
        model = BaseModel(id=custom_id)
        self.assertEqual(model.id, custom_id)

    def test_invalid_created_at_format_raises_exception(self):
        with self.assertRaises(ValueError):
            BaseModel(created_at="invalid_format")

    def test_invalid_updated_at_format_raises_exception(self):
        with self.assertRaises(ValueError):
            BaseModel(updated_at="invalid_format")
