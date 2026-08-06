import unittest
from app import is_valid_version, VERSION

class TestApp(unittest.TestCase):

    def test_version_format_is_valid(self):
        self.assertTrue(is_valid_version(VERSION))

    def test_invalid_version_is_rejected(self):
        self.assertFalse(is_valid_version("no-es-una-version"))

if __name__ == '__main__':
    unittest.main()