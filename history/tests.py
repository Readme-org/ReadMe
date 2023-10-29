from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import SearchHistory
import json

class HistoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.history_url = reverse('history:history')
        self.add_search_history_url = reverse('add_search_history')
        self.delete_history_ajax_url = reverse('delete_history_ajax')

    def test_history_GET(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.history_url)
        self.assertEqual(response.status_code, 200)

    def test_add_search_history_POST_invalid_method(self):
        response = self.client.get(self.add_search_history_url)
        self.assertEqual(response.status_code, 403)

    def test_add_search_history_POST_invalid_json(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.add_search_history_url, {}, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_search_history_POST_no_query(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.add_search_history_url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_search_history_POST_valid_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.add_search_history_url, json.dumps({"query": "test_query"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete_history_ajax_invalid_method(self):
        response = self.client.get(self.delete_history_ajax_url)
        self.assertEqual(response.status_code, 403)

    def test_delete_history_ajax_valid_delete(self):
        self.client.login(username='testuser', password='testpassword')
        history = SearchHistory.objects.create(user=self.user, query="test_query")
        response = self.client.post(self.delete_history_ajax_url, {"history_id": history.id})
        self.assertEqual(response.status_code, 200)

    def test_delete_history_ajax_invalid_id(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_history_ajax_url, {"history_id": 999})
        self.assertEqual(response.status_code, 400)
