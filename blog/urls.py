from django.urls import path
from .views import PostListView, PostDetailView, ContactCreateView, NewsletterCreateView
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('privacy/', views.privacy, name='blog-privacy'),
	path('terms/', views.terms, name='blog-terms'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('blog/', PostListView.as_view(), name="blog-blog"),
	path('post/<slug>/', PostDetailView.as_view(), name="post-detail"),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('books/', views.books, name='blog-books'),
	path('books/entrepreneurship', views.books_entrepreneurship, name='blog-books-entrepreneurship'),
	path('books/personal_growth', views.books_personal_growth, name='blog-books-personal-growth'),
	path('books/philosophy', views.books_philosophy, name='blog-books-philosophy'),
	path('books/psychology', views.books_psychology, name='blog-books-psychology'),
	path('books/society', views.books_society, name='blog-books-society'),
	path('newsletter/', NewsletterCreateView.as_view(), name='blog-newsletter'),
]

