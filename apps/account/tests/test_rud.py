from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth import authenticate
from ..models import Account


class AccountListTestCase(APITestCase):
    def setUp(self):
        # Creating data for Account model
        Account.objects.create_user(
            username='test',
            password='123'
        )

    def test_get_list(self):
        user = authenticate(username='test', password='123')
        if user:
            self.client.force_authenticate(user=user)

            response = self.client.get('/account/list/')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.fail("Authentication failed for user admin.")


class AccountDetailTestCase(APITestCase):
    def setUp(self):
        # Creating data for Account model
        self.user = Account.objects.create_user(
            username='test',
            password='123'
        )
        self.client.force_authenticate(user=self.user)
        self.detail_url = f'/account/detail/update/{self.user.id}/'

    def test_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['username'], 'test')


class AccountPatchTestCase(APITestCase):
    def setUp(self):
        # Creating data for Account model
        self.user = Account.objects.create_user(
            username='test',
            password='123'
        )
        self.client.force_authenticate(user=self.user)
        self.update_url = f'/account/detail/update/{self.user.id}/'

    def test_patch(self):
        data = {
            'username': 'test1'
        }
        response = self.client.patch(self.update_url, data)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.user.username, 'test1')


class AccountPutTestCase(APITestCase):
    def setUp(self):
        # Creating data for Account model
        self.user = Account.objects.create_user(
            username='test',
            password='123'
        )
        self.client.force_authenticate(user=self.user)
        self.update_url = f'/account/detail/update/{self.user.id}/'

    def test_put(self):
        data = {
            'username': 'test1',
            'password': '12345'
        }
        response = self.client.patch(self.update_url, data)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.user.username, 'test1')