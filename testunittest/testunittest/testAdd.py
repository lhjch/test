from calculator import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test setup")

    def tearDown(self):
        print("test teardown")

    def testadd(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        print("testadd")

    def testadd2(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        print("testadd2")

    def add3(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        print("add3")

if __name__ == "__main__":
    unittest.main()