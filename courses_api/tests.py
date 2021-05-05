from django.test import TestCase, Client
from .models import Course
import requests


class ViewsTest(TestCase):
    def setUp(self) -> None:
        c = Course.objects.create(
                                  name="only a test", 
                                  start_date="2020-12-12T20:20:00Z", 
                                  expiration_date="2020-12-12T20:20:00Z", 
                                  lecture_quantity=12,
                                  )
        self.client = Client()

    def test_get(self):
        response = requests.get('http://127.0.0.1:8000/course/')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = requests.delete('http://127.0.0.1:8000/course/?pk=1')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
                'name': 'test',
                'start_date': '2020-12-24T20:47:00Z',
                'expiration_date': '2020-12-30T20:47:00Z',
                'lecture_quantity': 10,
        }

        response = requests.post('http://127.0.0.1:8000/course/',
                                json=data
                                )
        self.assertEqual(response.status_code, 200)
        self.assertIn('test', response.text)

    def test_put(self):
        data = {
            'name': 'test10',
            'start_date': '2020-12-24T20:47:00Z',
            'expiration_date': '2020-12-30T20:47:00Z',
            'lecture_quantity': 10,
        }
        response = requests.put('http://127.0.0.1:8000/course/?pk=1',
                                data
                                )
        print(response.status_code)                       
        self.assertEqual(response.status_code, 200)
        self.assertIn('test10', response.text)


