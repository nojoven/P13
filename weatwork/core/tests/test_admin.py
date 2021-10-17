from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # Setup will be called first
    def setUp(self):
        # This client will be used to send http requests
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@maintanerdev.com", password="password123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="test@maintainerdev.com",
            password="password123",
            name="Test user full name",
            tiktok="https://www.tiktok.com/users/user/mdev1",
            twitch="https://www.twitch.com/users/user/mdev1",
            quora="https://www.quora.com/users/user/mdev1",
            linkedin="https://www.linkedin.com/users/user/mdev1",
            instagram="https://www.instagram.com/users/user/mdev1",
            youtube="https://www.youtube.com/users/user/mdev1",
            twitter="https://www.twitter.com/users/user/mdev1",
            snapchat="https://www.snapchat.com/users/user/mdev1",
            udemy="https://www.snapchat.com/users/user/mdev1",
            gitlab="https://www.gitlab.com/users/user/mdev1",
            github="https://www.github.com/users/user/mdev1",
            bitbucket="https://www.bitbucket.com/users/user/mdev1",
        )

    def test_users_listed(self):
        """Tests that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Tests that the edit user page works"""
        # /admin/core/user/
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Tests that the create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
