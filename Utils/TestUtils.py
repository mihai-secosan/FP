from Utils import *
import unittest

class TestUtilsMethods(unittest.TestCase):

    def test_str2cif(self):
        self.assertEqual(str2cif(0), '00')
        self.assertEqual(str2cif(5), '05')
        self.assertEqual(str2cif(10), '10')
        self.assertEqual(str2cif(52), '52')
        self.assertEqual(str2cif(70), '70')
        self.assertEqual(str2cif(100), '00')
        self.assertEqual(str2cif(12345), '45')

    def test_str4cif(self):
        self.assertEqual(str4cif(0), '0000')
        self.assertEqual(str4cif(5), '0005')
        self.assertEqual(str4cif(10), '0010')
        self.assertEqual(str4cif(100), '0100')
        self.assertEqual(str4cif(1000), '1000')
        self.assertEqual(str4cif(10000), '0000')
        self.assertEqual(str4cif(123), '0123')
        self.assertEqual(str4cif(123456), '3456')
        self.assertEqual(str4cif(12340), '2340')

    def test_opus(self):
        self.assertEqual(opus({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '<'}), {'criteriu': 'user', 'reper': 'meHIGH', 'semn': '>='})

    def test_cleanList(self):
        self.assertEqual(cleanList([1, '', ['', '', 1, []], 12, '', 123, [123, 'p'], 1234]), [1, 1, 12, 123, 123, 'p', 1234])
