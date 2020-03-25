from django.shortcuts import render
from .models import Course, Path
	
def courses(request):
	context = {
	'courses_personal_growth': Course.objects.filter(paths=2),
	'courses_entrepreneurship': Course.objects.filter(paths=3),
	'courses_philosophy': Course.objects.filter(paths=5),
	'courses_psychology': Course.objects.filter(paths=6),
	'courses_society': Course.objects.filter(paths=7),
	'courses': Course.objects.all(),
	'title': 'All Essays' 
	}
	return render(request, 'learn/courses.html', context)	

def course_details(request, slug):
	context = {
	'course': Course.objects.get(slug=slug),
	'title': Course.objects.get(slug=slug).course_title,
	}
	return render(request, 'learn/course_details.html', context)

def courses_entrepreneurship(request):
	context = {
	'courses_entrepreneurship': Course.objects.filter(paths=3),
	'title': 'Essays on Work'
	}
	return render(request, 'learn/courses_entrepreneurship.html', context)

def courses_personal_growth(request):
	context = {
	'courses_personal_growth': Course.objects.filter(paths=2),
	'title': 'Essays on Personal Growth'
	}
	return render(request, 'learn/courses_personal_growth.html', context)

def courses_philosophy(request):
	context = {
	'courses_philosophy': Course.objects.filter(paths=5),
	'title': 'Essays on Thinking'
	}
	return render(request, 'learn/courses_philosophy.html', context)

def courses_psychology(request):
	context = {
	'courses_psychology': Course.objects.filter(paths=6),
	'title': 'Essays on Self-Knowledge'
	}
	return render(request, 'learn/courses_psychology.html', context)

def courses_society(request):
	context = {
	'courses_society': Course.objects.filter(paths=7),
	'title': 'Essays on Society'
	}
	return render(request, 'learn/courses_society.html', context)