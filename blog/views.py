from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Contact, Books, Newsletter
from learn.models import Path

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title': 'Educator and Consultant'})

class PostListView(ListView):
	model = Post
	template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

class WebDevPostListView(ListView):
	model = Post
	template_name = 'blog/category_web_dev.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	queryset = Post.objects.filter(category=1)
	ordering = ['-date_posted']


class WebDesignPostListView(ListView):
	model = Post
	template_name = 'blog/category_web_design.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	queryset = Post.objects.filter(category=4)
	ordering = ['-date_posted']

class EntrepreneurshipPostListView(ListView):
	model = Post
	template_name = 'blog/category_entrepreneurship.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	queryset = Post.objects.filter(category=3)
	ordering = ['-date_posted']

class PersonalGrowthPostListView(ListView):
	model = Post
	template_name = 'blog/category_personal_growth.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	queryset = Post.objects.filter(category=2)
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	
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

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('name')
#             messages.success(request, f'Your message has been sent!')
#             return redirect('contact')
#     else:
#         form = ContactForm()

#     context = {
#     'form': form,
#     'title': 'Contact'
#     }
#     return render(request, 'blog/contact.html', context)

def books(request):
	context = {
	'books_web_development': Books.objects.filter(category=1),
	'books_personal_growth': Books.objects.filter(category=2),
	'books_entrepreneurship': Books.objects.filter(category=3),
	'books_web_design': Books.objects.filter(category=4),
	'title': 'Recommended Books' 
	}
	return render(request, 'blog/books.html', context )

