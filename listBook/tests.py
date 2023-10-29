from django.test import TestCase, Client
from django.contrib.auth.models import User
from listBook.models import myBook
from main.models import Book

class ListBookTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        self.book = Book.objects.create(title='Test Book', authors='Test Author', genre='action')
        self.mybook = myBook.objects.create(user=self.user, title='My Test Book', authors='Test Author', image='image_url', description='Test Description', isbn='12345', display_title='My Test Book')

    def test_show_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/list-book/list-book')
        self.assertEqual(response.status_code, 200)

    def test_show_list_filter(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/list-book/list-book-filter/action/')
        self.assertEqual(response.status_code, 200)

    def test_show_list_title(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/list-book/show_list_title/', {'title': 'Test'})
        self.assertEqual(response.status_code, 200)

    def test_show_myBook(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/list-book/my-book')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('/list-book/add-book/', {
            'title': 'New Book',
            'authors': 'New Author',
            'image': 'new_image_url',
            'description': 'New Description',
            'isbn': '67890',
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(myBook.objects.filter(title='New Book').exists())

    def test_delete_book(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(f'/list-book/delete-book/{self.mybook.id}/')
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertFalse(myBook.objects.filter(id=self.mybook.id).exists())

    

# def test_show_list_filter(self):
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.get('/list-book/list-book-filter/action/')
