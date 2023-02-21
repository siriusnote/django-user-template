"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(username='testing_user', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(username, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_username_successful(self):
        """Test creating a user with username is successful."""
        username = 'testing_user'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_username_normalized(self):
        """Test username is normalized for new users."""
        sample_usernames = [
            ['\u0066\u0066', 'ff'],
        ]

        for username, expected in sample_usernames:
            user = get_user_model().objects.create_user(username, 'sample123')
            self.assertEqual(user.username, expected)

    def test_new_user_without_username_raises_error(self):
        """Test that creating a user without username raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'admin',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
