from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from pawssearch.posts.models import Posts
from pawssearch.posts.forms import PostForm

UserModel = get_user_model()


class PostFormTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='password123')

    def test_valid_post_form(self):
        form_data = {
            'title': 'Lost Dog',
            'description': 'My dog is lost, please help.',
            'pet_type': 'DOG',
            'post_type': 'MISSING',
            'contact_info': '123456789',
            'image': 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg',
            'region': 'SOFIA',
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_post_form_missing_title(self):
        form_data = {
            'description': 'My dog is lost, please help.',
            'pet_type': 'DOG',
            'post_type': 'MISSING',
            'contact_info': '123456789',
            'image': 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg',
            'region': 'SOFIA',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_invalid_post_form_invalid_url(self):
        form_data = {
            'title': 'Lost Dog',
            'description': 'My dog is lost, please help.',
            'pet_type': 'DOG',
            'post_type': 'MISSING',
            'contact_info': '123456789',
            'image': 'invalid-url',
            'region': 'SOFIA',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)


class PostViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='test_user', password='password123')

    def test_create_post_view(self):
        self.client.login(username='test_user', password='password123')
        response = self.client.post(reverse('create post'), {
            'title': 'Lost Dog',
            'description': 'My dog is lost.',
            'pet_type': 'DOG',
            'post_type': 'MISSING',
            'contact_info': '123456789',
            'image': 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg',
            'region': 'SOFIA',
        })
        self.assertRedirects(response, reverse('user posts'))
        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(Posts.objects.first().title, 'Lost Dog')

    def test_edit_post_view(self):
        self.client.login(username='test_user', password='password123')
        post = Posts.objects.create(
            title='Lost Dog',
            description='My dog is lost.',
            pet_type='DOG',
            post_type='MISSING',
            user=self.user
        )
        response = self.client.post(reverse('edit post', args=[post.pk]), {
            'title': 'Found Dog',
            'description': 'I found the dog.',
            'pet_type': 'DOG',
            'post_type': 'FOUND',
            'contact_info': '987654321',
            'image': 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg',
            'region': 'SOFIA',
        })
        self.assertRedirects(response, reverse('user posts'))
        post.refresh_from_db()
        self.assertEqual(post.title, 'Found Dog')

    def test_delete_post_view(self):
        self.client.login(username='test_user', password='password123')
        post = Posts.objects.create(
            title='Lost Dog',
            description='My dog is lost.',
            pet_type='DOG',
            post_type='MISSING',
            user=self.user
        )
        response = self.client.post(reverse('delete post', args=[post.pk]))
        self.assertRedirects(response, reverse('user posts'))
        self.assertEqual(Posts.objects.count(), 0)

    def test_detail_post_view(self):
        self.client.login(username='test_user', password='password123')
        post = Posts.objects.create(
            title='Lost Dog',
            description='My dog is lost.',
            pet_type='DOG',
            post_type='MISSING',
            user=self.user
        )
        response = self.client.get(reverse('detail post', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
