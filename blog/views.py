from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Contact, Books, Newsletter
from learn.models import Path

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title': 'Education for curious learners'})

class PostListView(ListView):
	model = Post
	template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	
class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'

def ContactSuccess(request):
	return render(request, 'blog/contact_success.html')

class NewsletterCreateView(CreateView):
	model = Newsletter
	fields = ['email']

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def books(request):
	context = {
	'books_personal_growth': Books.objects.filter(category=2),
	'books_entrepreneurship': Books.objects.filter(category=3),
	'books_philosophy': Books.objects.filter(category=5),
	'books_psychology': Books.objects.filter(category=6),
	'title': 'Recommended Books' 
	}
	return render(request, 'blog/books.html', context )

