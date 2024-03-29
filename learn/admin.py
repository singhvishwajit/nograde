from django.contrib import admin
from .models import Category, Essay
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class EssayAdmin(admin.ModelAdmin):
	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Category)
admin.site.register(Essay, EssayAdmin)
