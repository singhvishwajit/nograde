from django.db import models

# Create your models here.
# Examples of Paths could be web development, data science, entrepreneurship, personal growth, etc.
# Examples of Courses could be Introduction to Python, Git, Command Line. 
# All the above example courses can be part of both data science and web development paths. 
# Therefore each path can have many courses and each course could be part of many paths. 
# Similarly, each course will have many tutorials and each tutorial can be part of many courses. 


class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_details = models.CharField(max_length=100)
	slug = models.SlugField(default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.category_name}"

class Essay(models.Model):
	categories = models.ManyToManyField(Category, blank=True)
	essay_title = models.CharField(max_length=100)
	slug = models.SlugField(default="some-string")
	essay_details = models.TextField()
	essay_content = models.TextField(default="hello")
	thumbnail = models.ImageField(default='default.png', blank=True)
	alt_text = models.TextField(default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.essay_title}"

