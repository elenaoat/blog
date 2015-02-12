from django.test import TestCase
from blogengine.models import Post
from django.utils import timezone


class TestPost(TestCase):

	def test_post_exists(self):
		p = Post()
		p.title = 'Review on book'
		p.text = 'Here comes my review'
		p.pub_date = timezone.now()

		p.save()

		post = Post.objects.get(title__contains='on book')
		self.assertEquals(post, p)

		self.assertEquals(post.title, p.title)



