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
	skills_covered = models.TextField()
	thumbnail = models.ImageField(default='default.png', blank=True)
	prerequisites = models.CharField(max_length=100, default="some-string")

	# add in thumbnail

	def __str__(self):
		return f"{self.id} - {self.course_title}"


class Guide(models.Model):
	guide_title = models.CharField(max_length=100)
	slug = models.SlugField()
	guide_details = models.TextField()
	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
	guide_snippet = models.CharField(max_length=100, default='some-string')

	def __str__(self):
		return self.guide_title




class Syllabus(models.Model):
	lesson_num = models.CharField(max_length=100)
	lesson_title = models.CharField(max_length=100)
	lesson_overview = models.TextField()
	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.course_name}-{self.lesson_num}"

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=100)
	tutorial_content = models.TextField()
	courses = models.ManyToManyField(Course, blank=True, related_name="tutorials")

	def __str__(self):
		return f"{self.id} - {self.tutorial_title}"