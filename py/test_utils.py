import unittest

from xcal_common.py.error import ECommonFileNotExist
from xcal_common.py.utils import get_error_message


class MyTestCase(unittest.TestCase):
    def test_get_error_message_ok(self):
        error_message = get_error_message(ECommonFileNotExist())
        self.assertIsNotNone(error_message)

    def test_get_error_message_with_builtin_error_name(self):
        with self.assertRaises(AssertionError):
            get_error_message(FileNotFoundError())


if __name__ == '__main__':
    unittest.main()
