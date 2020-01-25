from django.urls import path


from . import views

urlpatterns = [
	path('', views.home, name='learn-home'),
	path('courses/', views.courses, name='learn-courses'),
	path('guides/', views.guides, name='learn-guides'),
	path('courses/entrepreneurship', views.courses_entrepreneurship, name='learn-courses-entrepreneurship'),
	path('courses/personal-growth', views.courses_personal_growth, name='learn-courses-personal-growth'),
	path('courses/philosophy', views.courses_philosophy, name='learn-courses-philosophy'),
	path('courses/psychology', views.courses_psychology, name='learn-courses-psychology'),
	path('courses/<slug:slug>/', views.course_details, name='learn-course-details'),
	path('guides/<slug:slug>/', views.guide_details, name='learn-guide-details'),
]

