from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

class MemberAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_member(self):
        body = {
            "username": "username1234",
            "password": "password1234",
            "email": "abc@abc.com"
        }

        resp = self.client.post(reverse("member:create"), body)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        member = User.objects.filter(username=body['username'])
        self.assertEqual(member.exists(), True)
        self.assertEqual(member.first().email, body['email'])

    def test_create_member_token(self):
        body = {
            "username": "username1234",
            "password": "password1234",
            "email": "abc@abc.com"
        }

        user = User.objects.create_user(**body)

        body = {
            "username": "username1234",
            "password": "password1234"
        }
        resp = self.client.post(reverse("member:token"), body)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)

    def test_get_profile_wo_auth(self):
        # Unauthorized user testing
        resp = self.client.get(reverse("member:profile"))
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile_with_auth(self):
        body = {
            "username": "username1234",
            "password": "password1234",
            "email": "abc@abc.com"
        }

        user = User.objects.create_user(**body)
        self.client.force_authenticate(user=user)

        resp = self.client.get(reverse("member:profile"))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['email'], body['email'])

    def test_patch_member_email(self):
        body = {
            "username": "username1234",
            "password": "password1234",
            "email": "abc@abc.com"
        }

        user = User.objects.create_user(**body)
        self.client.force_authenticate(user=user)

        body = {
            "email": "abcd@abcd.com"
        }

        resp = self.client.patch(reverse("member:profile"), body)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['email'], body['email'])
