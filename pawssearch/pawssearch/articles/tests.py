from django.test import TestCase
from .models import Article
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticlesTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(username='staffuser', password='TestPass123', email='teststaffuser@example.com', is_staff=True)
        self.article = Article.objects.create(
            title="Sample Article",
            url="https://www.pexels.com/search/dog/"
        )

    def test_article_list_view(self):
        response = self.client.get(reverse('all article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/all_article.html')
        self.assertContains(response, self.article.title)

    def test_article_add_view_as_staff(self):
        self.client.login(username='staffuser', password='TestPass123')
        response = self.client.post(reverse('add article'), {
            'title': 'New Article',
            'url': 'https://www.pexels.com/search/dog/'
        })
        self.assertRedirects(response, reverse('all article'))
        self.assertTrue(Article.objects.filter(title='New Article').exists())

    def test_article_edit_view_as_staff(self):
        self.client.login(username='staffuser', password='TestPass123')
        response = self.client.post(reverse('edit article', args=[self.article.pk]), {
            'title': 'Updated Title',
            'url': 'https://www.pexels.com/search/dog/'
        })
        self.assertRedirects(response, reverse('all article'))
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Title')

    def test_article_delete_view_as_staff(self):
        self.client.login(username='staffuser', password='TestPass123')
        response = self.client.post(reverse('delete article', args=[self.article.pk]))
        self.assertRedirects(response, reverse('all article'))
        self.assertFalse(Article.objects.filter(pk=self.article.pk).exists())
