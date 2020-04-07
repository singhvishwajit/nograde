from django.urls import path
from .views import PostListView, PostDetailView, ContactCreateView, NewsletterCreateView
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('privacy/', views.privacy, name='blog-privacy'),
	path('terms/', views.terms, name='blog-terms'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('guides/', PostListView.as_view(), name="blog-guides"),
	path('guide/<slug>/', PostDetailView.as_view(), name="guide-detail"),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('books/', views.books, name='blog-books'),
	path('books/work', views.books_work, name='blog-books-work'),
	path('books/personal-growth', views.books_personal_growth, name='blog-books-personal-growth'),
	path('books/thinking', views.books_thinking, name='blog-books-thinking'),
	path('books/self-knowledge', views.books_self_knowledge, name='blog-books-self-knowledge'),
	path('books/society', views.books_society, name='blog-books-society'),
	path('newsletter/', NewsletterCreateView.as_view(), name='blog-newsletter'),
]

