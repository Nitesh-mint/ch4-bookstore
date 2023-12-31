from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review

class BookTest(TestCase):

    # @classmethod makes the class a static method like in java
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "reviewuser",
            email = "reviewuser@email.com",
            password = "testpass123",
        )

        cls.special_permission = Permission.objects.get(
            codename = "special_status"
        )

        cls.book = Book.objects.create(
            title = "Atomic Habits",
            author = "James Clear",
            price = "2500",
        )

        cls.review = Review.objects.create(
            book = cls.book,
            author = cls.user,
            review = "Nice Book",
        )
    
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Atomic Habits")
        self.assertEqual(f"{self.book.author}", "James Clear")
        self.assertEqual(f"{self.book.price}", "2500")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Atomic Habits")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" % (reverse("account_login")))
        response = self.client.get("%s?next=/books/" % (reverse("account_login")))
        self.assertContains(response, "Log In")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testpass123") 
        self.user.user_permissions.add(self.special_permission)
        # response = self.client.get(self.book.get_absolute_url())
        # no_response = self.client.get("/books/12345/")
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        # self.assertContains(response, "Atomic Habits")
        # self.assertContains(response, "Nice Book")
        # self.assertTemplateUsed(response, "books/book_detail.html")


