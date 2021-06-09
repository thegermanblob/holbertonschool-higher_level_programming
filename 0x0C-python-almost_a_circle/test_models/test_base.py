#!/usr/bin/python3
""" Module that contains unittest for class Base """
import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """ test class """

    def test_pep8_coformance(self):
        """ Test that we conforms PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'models/base.py', '../test_models/test_base'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def setUp(self):
        """ sets up the class for testing """
        self.b1 = Base(21)
        self.b2 = Base(-21)
        self.b3 = Base(0)
        self.b4 = Base({'hi': 'hello', 'hey': "jaja"})
        self.b5 = Base(None)
        self.b6 = Base()

    def test_empty_constructors(self):
        """ tests if counter is working """
        self.assertEqual(self.b5.id, 1)
        self.assertEqual(self.b6.id, 2)
        self.assertEqual(self.b3.id, 0)


    def tearDown(self):
        pass
