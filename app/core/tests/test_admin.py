from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        email = "admin@email.com"
        password = "pass123word456"
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.client.force_login(self.admin_user)

        email = "user@email.com"
        password = "pass789word012"

        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name="Test User"
        )

    def test_users_listed(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse("admin:core_user_change", args=[self.user.id])
        # / admin/core/user/[self.user.id]
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
