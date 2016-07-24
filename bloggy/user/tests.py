from django.test import TestCase

# coding=utf-8
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class TestUser(TestCase):
    def test_login(self):
        User = get_user_model()
        user = User.objects.create(
            email='test@test.com')
        user.set_password('test')
        user.save()
        result = authenticate(username='test@test.com', password='test')
        self.assertEqual(result, user)
