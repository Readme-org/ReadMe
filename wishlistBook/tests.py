from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from listBook.models import myBook
from wishlistBook.models import WishlistBook

class WishlistViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.book = myBook.objects.create(title="Test Book", author="Test Author")
        self.wishlist = WishlistBook.objects.create(user=self.user, book=self.book)

    def test_show_wishlist(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('wishlistBook:show_wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')  # Pastikan judul buku ada di tampilan

    def test_get_books_json_created(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('wishlistBook:get_books_json', args=[self.book.id]))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content, b'CREATED')

    def test_get_books_json_already_exist(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('wishlistBook:get_books_json', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ALREADY EXIST')

    def test_deleteWishlist(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('wishlistBook:deleteWishlist', args=[self.wishlist.id]))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content, b'DELETED')

    def test_deleteWishlist_not_found(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('wishlistBook:deleteWishlist', args=[999]))  # ID yang tidak ada
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, b'NOT FOUND')
