from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, APIClient

from product.models import Book


class BookListTest(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        Book.create(name='abc', price='123')
        Book.create(name='张三', price=500.00)

    def test_book_list(self):
        self.assertEqual(Book.all().count(), 2)
