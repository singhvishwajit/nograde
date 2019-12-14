from django.urls import path
from .views import PostListView, PostDetailView, ContactCreateView,NewsletterCreateView, WebDevPostListView, WebDesignPostListView, EntrepreneurshipPostListView, PersonalGrowthPostListView
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
	path('about/', views.about, name='blog-about'),
	path('contact/', ContactCreateView.as_view(), name='blog-contact'),
	path('contact/success', views.ContactSuccess, name='blog-contact-success'),
	path('blog/', PostListView.as_view(), name='blog-blog'),
	path('blog/category/web-development', WebDevPostListView.as_view(), name='category-web-dev'),
	path('blog/category/web-design', WebDesignPostListView.as_view(), name='category-web-design'),
	path('blog/category/entrepreneurship', EntrepreneurshipPostListView.as_view(), name='category-entrepreneurship'),
	path('blog/category/personal-growth', PersonalGrowthPostListView.as_view(), name='category-personal-growth'),
	path('books/', views.books, name='blog-books'),
	path('newsletter/', NewsletterCreateView.as_view(), name='blog-newsletter'),
]