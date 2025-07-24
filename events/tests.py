from django.test import TestCase
from rest_framework.test import APIClient
from .models import Event

class EventTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.event = Event.objects.create(
            name="Test Event",
            location="Chennai",
            start_time="2025-07-25T10:00:00Z",
            end_time="2025-07-25T13:00:00Z",
            max_capacity=2
        )

    def test_register_attendee(self):
        url = f"/api/events/{self.event.id}/register"
        data = {"name": "Manoj", "email": "manoj@example.com"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
