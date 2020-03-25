from django.contrib import admin
from .models import Path, Course
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Path)
admin.site.register(Course, CourseAdmin)
