from calculator import Count
import unittest

class TestSubtract(unittest.TestCase):
    def setUp(self):
        print("test setup")

    def tearDown(self):
        print("test teardown")

    def testsubstract(self):
        j = Count(2,3)
        self.assertEqual(j.substract(),-1)
        print("testsubstract")

    def testsubstract2(self):
        j = Count(2,3)
        self.assertEqual(j.substract(),-1)
        print("testsubstract2")

    def substract3(self):
        j = Count(2,3)
        self.assertEqual(j.add(),-1)
        print("add3")

if __name__ == "__main__":
    unittest.main()