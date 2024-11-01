from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from pawssearch.posts.models import Posts
from pawssearch.main.models import Comment, Follow
from django.core import mail

User = get_user_model()


class UserOpinionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testimonialuser", password="TestPass123", email="test@example.com")
        self.client.login(username="testimonialuser", password="TestPass123")

    def test_submit_testimonial(self):
        response = self.client.post(reverse('submit_testimonial'), {'testimonial': 'Great website!'})
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('New User Opinion', mail.outbox[0].subject)
        self.assertIn('Great website!', mail.outbox[0].body)


class ContactViewTests(TestCase):
    def test_contact_message_sent(self):
        response = self.client.post(reverse('contact'), {
            'email': 'user@example.com',
            'phone': '1234567890',
            'message': 'Hello, I need help!'
        })
        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Contact Us - Inquiry', mail.outbox[0].subject)
        self.assertIn('Hello, I need help!', mail.outbox[0].body)
