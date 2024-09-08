""" Test Joy model in models.py """
from django.test import TestCase
from joylist.models import Joy


class TestJoyModel(TestCase):
    def test_str(self):
        """ Test string representation method
            Parameters:
                self: current testcase
        """
        print("str rep tested")
        joy = Joy(title='TestJoyModel', desc="Test desc")
        self.assertEqual(str(joy.title), "TestJoyModel")
