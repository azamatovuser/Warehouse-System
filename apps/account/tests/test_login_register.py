from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth import authenticate
from ..models import Account


class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.login_url = '/account/login/'

    def test_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('access', response.data['data']['tokens'])
        self.assertIn('refresh', response.data['data']['tokens'])


class RegisterTestCase(APITestCase):

    def setUp(self):
        self.register_url = '/account/register/'

    def test_register(self):
        response = self.client.post(self.register_url, {
            'username': 'supportjon',
            'password': 'Pass!123',
            'password2': 'Pass!123',
            'role': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('access', response.data['data']['tokens'])
        self.assertIn('refresh', response.data['data']['tokens'])

    def test_register_invalid_data(self):
        response = self.client.post(self.register_url, {
            'username': 'supportjon',
            'password1': 'Pass!123',
            'password2': 'WrongPassword',
            'role': 1,
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)