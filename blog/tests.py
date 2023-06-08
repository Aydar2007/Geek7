from django.test import TestCase, Client
from django.urls import reverse


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # reverse по имени эндпоинта "index-page" возвращает строку http://127.0.0.1:8000/
        response = self.client.get(reverse("index-page"))
        exp_data = "Main page"
        self.assertEqual(exp_data, response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_test_page(self):
        # reverse по имени эндпоинта "test-page" возвращает строку http://127.0.0.1:8000/test-page/
        response = self.client.get(reverse("test-page"))
        exp_data = "Test"
        self.assertEqual(exp_data, response.content.decode())
        self.assertEqual(response.status_code, 404)
