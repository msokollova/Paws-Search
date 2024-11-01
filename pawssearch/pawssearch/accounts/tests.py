from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsTests(TestCase):
    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'test_user',
            'email': 'testuser@example.com',
            'password1': 'TestPass123',
            'password2': 'TestPass123',
        })
        # Check for successful registration and redirect
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='test_user').exists())

    def test_login_view(self):
        user = User.objects.create_user(username="test_user", password="TestPass123")
        response = self.client.post(reverse('login'), {
            'username': 'test_user',
            'password': 'TestPass123',
        })
        self.assertRedirects(response, reverse('index'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_edit_profile_view(self):
        user = User.objects.create_user(username="test_user", password="TestPass123", email="old@example.com")
        self.client.force_login(user)
        response = self.client.post(reverse('edit profile', args=[user.pk]), {
            'first_name': 'NewFirst',
            'last_name': 'NewLast',
            'email': 'new@example.com',
        })
        self.assertRedirects(response, reverse('index'))
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'NewFirst')
        self.assertEqual(user.email, 'new@example.com')

    def test_password_change_view(self):
        user = User.objects.create_user(username="test_user", password="TestPass123")
        self.client.force_login(user)
        response = self.client.post(reverse('change password', args=[user.pk]), {
            'old_password': 'TestPass123',
            'new_password1': 'NewPass123!',
            'new_password2': 'NewPass123!',
        })
        self.assertRedirects(response, reverse('password change done'))
        user.refresh_from_db()
        self.assertTrue(user.check_password('NewPass123!'))
