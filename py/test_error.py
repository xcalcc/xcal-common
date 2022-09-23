import unittest


class MyTestCase(unittest.TestCase):
    def test_import_error_file(self):
        try:
            import py.error
        except SyntaxError as e:
            print(e)
            self.assertFalse(True)
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
