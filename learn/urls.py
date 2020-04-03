from django.urls import path


from . import views

urlpatterns = [
	path('all', views.courses, name='all-essays'),
	path('work', views.courses_entrepreneurship, name='essays-work'),
	path('personal-growth', views.courses_personal_growth, name='essays-personal-growth'),
	path('thinking', views.courses_philosophy, name='essays-thinking'),
	path('self-knowledge', views.courses_psychology, name='essays-self-knowledge'),
	path('society', views.courses_society, name='essays-society'),
	path('<slug:slug>/', views.course_details, name='essay-details'),
]

