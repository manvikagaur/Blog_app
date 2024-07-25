from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Post, Comment

class BlogAppAdminTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_post_creation(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.author, self.user)
        self.assertEqual(str(post), 'Test Post')

    def test_comment_creation(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, author=self.user, text='Test Comment')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.text, 'Test Comment')
        self.assertEqual(str(comment), f'Comment by {self.user.username} on {post}')

    def test_post_list(self):
        url = reverse('post-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'New Post')

    def test_post_retrieve(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', args=[post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)

    def test_post_update(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(post.content, 'Updated Content')

    def test_post_delete(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_comment_list(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('comment-list-create', args=[post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
