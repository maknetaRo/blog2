from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        self.post = Post.objects.create(
            title="A good title", text="Nice body content", author=self.user,
        )

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.text}", "Nice body content")

    def test_post_list_view(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")


class HomePageTEst(TestCase):
    def test_uses_base_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")


class AboutPageTest(TestCase):
    def test_uses_about_template(self):
        response = self.client.get("/about")
        self.assertTemplateUsed(response, "blog/about.html")
