from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, board_posts
from .models import Board

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Other', description='Other images with no specification')
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_posts_page(self):
        board_posts_url = reverse('board_posts', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_posts))

class BoardPostsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Other', description='Other images with no specification')

    def test_board_posts_view_success_status_code(self):
        url      = reverse('board_posts', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_posts_view_not_found_status_code(self):
        url      = reverse('board_posts', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_posts_url_resolves_board_posts_view(self):
        views    = resolve('/boards/1')
        self.assertEquals(view.func, board_posts)

    def test_board_posts_view_contains_link_back_to_homepage(self):
        board_posts_url = reverse('board_posts', kwargs={'pk': 1})
        response        = self.client.get(board_posts_url)
        homepage_url    = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewPostTest(TestCase):
    def setUp(self):
        Board.objects.create(name='Other', description='Other images with no specification')

    def test_new_post_view_success_status_code(self):
        url = reverse('new_post', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_post_view_not_found_status_code(self):
        url = reverse('new_post', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_post_url_resolves_new_post_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_post)

    def test_new_post_view_contains_link_back_to_board_posts_view(self):
        new_post_url = reverse('new_post', kwargs={'pk': 1})
        board_posts_url = reverse('board_posts', kwargs={'pk': 1})
        response = self.client.get(new_post_url)
        self.assertContains(response, 'href="{0}"'.format(board_posts_url))