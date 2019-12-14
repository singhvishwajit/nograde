from django.urls import path


from . import views

urlpatterns = [
	path('', views.home, name='learn-home'),
	path('courses/', views.courses, name='learn-courses'),
	path('guides/', views.guides, name='learn-guides'),
	path('courses/web-development', views.courses_web_dev, name='learn-courses-web-dev'),
	path('courses/web-design', views.courses_web_design, name='learn-courses-web-design'),
	path('courses/entrepreneurship', views.courses_entrepreneurship, name='learn-courses-entrepreneurship'),
	path('courses/personal-growth', views.courses_personal_growth, name='learn-courses-personal-growth'),
	path('courses/<slug:slug>/', views.course_details, name='learn-course-details'),
	path('guides/<slug:slug>/', views.guide_details, name='learn-guide-details'),
]

