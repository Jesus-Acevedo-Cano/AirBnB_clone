#!/usr/bin/python3
""" State class unittests file"""
import os
import unittest
import models
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import time


class TestState(unittest.TestCase):
    """test class state"""

    def setUp(self):
        """create instances"""
        self.s1 = State()
        time.sleep(0.2)
        self.s2 = State()

    def test_create(self):
        """know egain if i can create a instance."""
        self.s3 = State()
        self.assertTrue(hasattr(self.s3, 'id'))

    def test_uuid(self):
        """know if id exist"""
        self.assertTrue(hasattr(self.s1, 'id'))

    def test_name_str(self):
        """know if name exists and is a string"""
        self.assertTrue(hasattr(self.s1, 'name'))
        self.assertTrue(isinstance(self.s1.name, str))

    def test_dif_id(self):
        """proof that the id are diferent"""
        self.assertNotEqual(self.s1.id, self.s2.id)

    def test_if_state(self):
        """know if the created object is State"""
        self.assertIsInstance(self.s1, State)

    def test_state_is_subclass(self):
        """proof if object is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.s1), BaseModel))

    def test_id_str(self):
        """know if id is of type string"""
        self.assertIsInstance(self.s1.id, str)

    def test_created_date(self):
        """test that the objects have diferent datetime"""
        self.assertNotEqual(self.s1.created_at, self.s2.created_at)

    def test_equal_date(self):
        """test if date of created and updated are same at"""
        self.assertEqual(self.s1.created_at, self.s1.updated_at)

    def test_update_dif(self):
        """proof that updated are diferent that created date when used"""
        self.s1.updated_at = datetime.now()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_created_at(self):
        """proof if created_at object exists"""
        self.assertTrue(hasattr(self.s1, 'created_at'))

    def test_updated_at(self):
        """proof if updated_at object exists"""
        self.assertTrue(hasattr(self.s1, 'updated_at'))

    def test_created_type(self):
        """know if created_at is a datetime object"""
        self.assertTrue(isinstance(self.s1.created_at, datetime))

    def test_updated_type(self):
        """know if updated_at is a datetime object"""
        self.assertTrue(isinstance(self.s1.updated_at, datetime))

    def test_input_dict(self):
        """know if it is posible to set attrbs as dict"""
        attrs = {"id": "1"}
        self.s1 = State(**attrs)
        self.assertEqual(attrs['id'], self.s1.id)

    def test_to_dict(self):
        """ giving created_at and updated_at values """
        date_frmt = "%Y-%m-%dT%H:%M:%S.%f"
        d = self.s1.to_dict()
        self.assertEqual(d["created_at"],
                         self.s1.created_at.strftime(date_frmt))
        self.assertEqual(d["updated_at"],
                         self.s1.updated_at.strftime(date_frmt))
        self.assertEqual(d["__class__"], "State")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_str(self):
        """know if the output string of the objects is correct"""
        output = "[{}] ({}) {}".format(
            self.s1.__class__.__name__,
            self.s1.id, self.s1.__dict__)
        self.assertEqual(str(self.s1), output)

    def test_docstring(self):
        """test docstring for the module and the class"""

        self.assertIsNotNone(models.state.__doc__,
            "No docstring in the module"
                                        )
        self.assertIsNotNone(State.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File state.py permissions"""

        test_file = os.access("models/state.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/state.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/state.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of State"""

        self.assertEqual(
            str(type(self.s1)),
            "<class 'models.state.State'>")
        self.assertIsInstance(self.s1, State)

if __name__ == '__main__':
    unittest.main()
