from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Contact, Books, Newsletter
from learn.models import Path

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
	model = Post
	template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	context['title'] = 'All Guides'
        	return context

class PostDetailView(DetailView):
	model = Post
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	slug = self.kwargs['slug']
        	context['title'] = Post.objects.get(slug=slug).title
        	return context
	
class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    success_url = 'success'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	context['title'] = 'Contact'
        	return context


def ContactSuccess(request):
	return render(request, 'blog/contact_success.html')

class NewsletterCreateView(CreateView):
	model = Newsletter
	fields = ['email']
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	context['title'] = 'Newsletter'
        	return context

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def books(request):
	context = {
	'books_personal_growth': Books.objects.filter(category=2),
	'books_entrepreneurship': Books.objects.filter(category=3),
	'books_philosophy': Books.objects.filter(category=5),
	'books_psychology': Books.objects.filter(category=6),
	'books_society': Books.objects.filter(category=7),
	'title': 'Recommended Books' 
	}
	return render(request, 'blog/books.html', context )

def books_entrepreneurship(request):
	context = {
	'books_entrepreneurship': Books.objects.filter(category=3),
	'title': 'Entrepreneurship Books'
	}
	return render(request, 'blog/books_entrepreneurship.html', context)

def books_personal_growth(request):
	context = {
	'books_personal_growth': Books.objects.filter(category=2),
	'title': 'Personal Growth Books'
	}
	return render(request, 'blog/books_personal_growth.html', context)

def books_philosophy(request):
	context = {
	'books_philosophy': Books.objects.filter(category=5),
	'title': 'Philosophy Books'
	}
	return render(request, 'blog/books_philosophy.html', context)

def books_psychology(request):
	context = {
	'books_psychology': Books.objects.filter(category=6),
	'title': 'Psychology Books'
	}
	return render(request, 'blog/books_psychology.html', context)

def books_society(request):
	context = {
	'books_society': Books.objects.filter(category=7),
	'title': 'Society Books'
	}
	return render(request, 'blog/books_society.html', context)

def handler404(request):
	return render(request, 'blog/404.html', status=404)


def privacy(request):
	context = {
	'title': 'Privacy'
	}
	return render(request, 'blog/privacy.html', context)

def terms(request):
	context = {
	'title': 'Terms'
	}
	return render(request, 'blog/terms.html', context)