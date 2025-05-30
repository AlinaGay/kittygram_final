"""
Test suite for the cats application API.

This module contains test cases for the Cat API endpoints, ensuring correct
behavior and access for authenticated users.
"""


from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class CatsAPITestCase(TestCase):
    """
    TestCase for Cat API endpoints.

    Sets up an authenticated user and tests the availability
    of the cat list endpoint.
    """

    def setUp(self):
        """
        Set up an authenticated user and API client for test cases.

        Creates a test user and authenticates the APIClient with this user
        to simulate authorized requests in the test methods.
        """
        user = get_user_model()
        self.user = user.objects.create_user(username='auth_user')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_exists(self):
        """Test cat list endpoint availability for authenticated users."""
        response = self.client.get('/api/cats/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
