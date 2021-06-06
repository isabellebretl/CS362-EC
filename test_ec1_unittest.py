import unittest
import ec1

class TestCase(unittest.TestCase):
    def test_leap1(self):
        self.assertEqual(ec1.main("Hello there"), "there Hello")
    def test_leap2(self):
        self.assertEqual(ec1.main("Hello"), "Hello")
    def test_leap3(self):
        self.assertEqual(ec1.main("Thanks for grading my extra credit"), "credit extra my grading for Thanks")


if __name__ == '__main__':
    unittest.main()