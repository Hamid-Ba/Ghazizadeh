"""Test For Admin"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminUserTest(TestCase):
    """Test For Admin User"""

    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            phone="09151498722", password="123456"
        )
        self.client = Client()

        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            phone="09151498712", first_name="Test User", last_name="Test User"
        )

    def test_access_to_user_list(self):
        """Tests User List"""
        url = reverse("admin:account_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.phone)
        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)

    def test_field_sets(self):
        """Tests User Field Sets List"""
        url = reverse("admin:account_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_add_filed_sets(self):
        """Tests User Add Field Sets List"""
        url = reverse("admin:account_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
