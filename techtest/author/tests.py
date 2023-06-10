import json

from django.test import TestCase
from django.urls import reverse

from .models import Author


class AuthorViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("authors-list")
        self.author_1 = Author.objects.create(first_name="John", last_name="Doe")
        self.author_2 = Author.objects.create(first_name="Jane", last_name="Smith")

    def test_serializes_single_record_with_correct_data_shape_and_status_code(self):
        url = reverse("author", kwargs={"author_id": self.author_1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.author_1.id,
                "first_name": "John",
                "last_name": "Doe",
            },
        )

    def test_creates_new_author(self):
        payload = {
            "first_name": "Alice",
            "last_name": "Johnson",
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 3)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "Alice",
                "last_name": "Johnson",
            },
            response.json(),
        )

    def test_updates_author(self):
        url = reverse("author", kwargs={"author_id": self.author_1.id})
        payload = {
            "id": self.author_1.id,
            "first_name": "Updated",
            "last_name": "Author",
        }
        response = self.client.put(
            url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.filter(id=self.author_1.id).first()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 2)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "Updated",
                "last_name": "Author",
            },
            response.json(),
        )

    def test_removes_author(self):
        url = reverse("author", kwargs={"author_id": self.author_1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.count(), 1)
