from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from learn.models import Path
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	slug = models.SlugField(default="some-string")
	category = models.ManyToManyField(Path, blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default='default.png', blank=True)

	# add in thumbnail

	def __str__(self):
		return self.title

	def snippet(self):
		return self.content[:500]


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()		

	def __str__(self):
		return self.name


class Books(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	thumbnail = models.ImageField(default='default.png', blank=True)
	category = models.ManyToManyField(Path, blank=True)
	details = models.TextField()
	amazon_url = models.URLField(default='google.com')

	def __str__(self):
		return self.title

class Newsletter(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email