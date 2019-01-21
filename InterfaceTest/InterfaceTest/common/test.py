from common.calculator import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print("test setup")

    def tearDown(self):
        print("test teardown")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        print("test_add")

    def test_add2(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        print("test_add2")

if __name__ == "__main__":
    unittest.main()