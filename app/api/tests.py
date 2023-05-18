from django.test import TestCase
from api.greet import say_hello


# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_dummy_test(self):
        self.assertEqual("hello", say_hello())
