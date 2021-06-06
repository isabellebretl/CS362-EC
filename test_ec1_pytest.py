import ec1
import pytest


class TestClass:
    def test_leap1(self):
        assert ec1.main("Hello there") == "there Hello"
    def test_leap2(self):
        assert ec1.main("Hello") == "Hello"
    def test_leap3(self):
        assert ec1.main("Thanks for grading my extra credit") == "credit extra my grading for Thanks"