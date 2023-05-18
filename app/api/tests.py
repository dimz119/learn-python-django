from django.test import SimpleTestCase, TestCase
from datetime import date
from rest_framework.test import APIClient
from unittest.mock import patch

from api.greet import function_to_get_today, say_hello


# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_dummy_test(self):
        self.assertEqual("hello", say_hello())


def fake_today():
    return date(year=2023, month=1, day=28)
 

class SampleTest(TestCase):
    @patch("api.greet.get_today", fake_today)
    def test_function_to_get_today_using_mock(self):
        self.assertEqual(function_to_get_today().strftime("%Y-%m-%d"), "2023-01-28")


class SimpleAPIClientTest(SimpleTestCase):
    def test_run_greetings(self):
        client = APIClient()
        resp = client.get('/api/greet/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, "hello")
