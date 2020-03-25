from django.db import models

# Create your models here.
# Examples of Paths could be web development, data science, entrepreneurship, personal growth, etc.
# Examples of Courses could be Introduction to Python, Git, Command Line. 
# All the above example courses can be part of both data science and web development paths. 
# Therefore each path can have many courses and each course could be part of many paths. 
# Similarly, each course will have many tutorials and each tutorial can be part of many courses. 


class Path(models.Model):
	path_name = models.CharField(max_length=100)
	path_details = models.CharField(max_length=100)
	slug = models.SlugField(default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.path_name}"

class Course(models.Model):
	paths = models.ManyToManyField(Path, blank=True)
	course_title = models.CharField(max_length=100)
	slug = models.SlugField(default="some-string")
	course_details = models.TextField()
	course_content = models.TextField(default="hello")
	thumbnail = models.ImageField(default='default.png', blank=True)
	alt_text = models.TextField(default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.course_title}"

