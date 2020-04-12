from django.contrib import admin
from .models import Post, Contact, Books, Newsletter
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {'fields': ["title", "date_posted"]}),
        ("Content", {"fields": ["content"]}),
        ("Slug", {"fields": ["slug"]}),
        ("Author", {"fields": ["author"]}),
        ("Thumbnail", {"fields": ["thumbnail"]})
    ]

	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}
	
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(Books)
admin.site.register(Newsletter)