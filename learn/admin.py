from django.contrib import admin
from .models import Path, Course, Tutorial, Syllabus, Guide
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}

class GuideAdmin(admin.ModelAdmin):
	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Path)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tutorial)
admin.site.register(Syllabus)
admin.site.register(Guide, GuideAdmin)
