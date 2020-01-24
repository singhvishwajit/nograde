from django.urls import path
from .views import PostListView, ContactCreateView, NewsletterCreateView
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('books/', views.books, name='blog-books'),
	path('newsletter/', NewsletterCreateView.as_view(), name='blog-newsletter'),
]