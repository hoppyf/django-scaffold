from django.test import TestCase, Client


class BookListTest(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        pass

    def test_book_list(self):
        pass
