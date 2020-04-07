from django.urls import path


from . import views

urlpatterns = [
	path('all', views.essays, name='all-essays'),
	path('work', views.essays_work, name='essays-work'),
	path('personal-growth', views.essays_personal_growth, name='essays-personal-growth'),
	path('thinking', views.essays_thinking, name='essays-thinking'),
	path('self-knowledge', views.essays_self_knowledge, name='essays-self-knowledge'),
	path('society', views.essays_society, name='essays-society'),
	path('<slug:slug>/', views.essay_details, name='essay-details'),
]

