from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_name = f'{post.text}'
        self.assertEqual(excepted_object_name, "just a test")



class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_location(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('posts_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('posts_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/list.html')
