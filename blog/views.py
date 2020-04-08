from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Contact, Books, Newsletter
from learn.models import Category

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
	success_url ='subscribed'
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        	context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        	context['title'] = 'Newsletter'
        	return context

def NewsletterSubscribed(request):
	return render(request, 'blog/newsletter_subscribed.html')

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def books(request):
	context = {
	'books_work': Books.objects.filter(categories=1),
	'books_thinking': Books.objects.filter(categories=2),
	'books_self_knowledge': Books.objects.filter(categories=3),
	'books_personal_growth': Books.objects.filter(categories=4),
	'books_society': Books.objects.filter(categories=5),
	'title': 'Recommended Books' 
	}
	return render(request, 'blog/books.html', context )

def books_work(request):
	context = {
	'books_work': Books.objects.filter(categories=1),
	'title': 'Books on Work'
	}
	return render(request, 'blog/books_work.html', context)

def books_thinking(request):
	context = {
	'books_thinking': Books.objects.filter(categories=2),
	'title': 'Books on Thinking'
	}
	return render(request, 'blog/books_thinking.html', context)


def books_self_knowledge(request):
	context = {
	'books_self_knowledge': Books.objects.filter(categories=3),
	'title': 'Books on Self-Knowledge'
	}
	return render(request, 'blog/books_self_knowledge.html', context)

def books_personal_growth(request):
	context = {
	'books_personal_growth': Books.objects.filter(categories=4),
	'title': 'Books on Personal Growth'
	}
	return render(request, 'blog/books_personal_growth.html', context)

def books_society(request):
	context = {
	'books_society': Books.objects.filter(categories=5),
	'title': 'Books on Society'
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