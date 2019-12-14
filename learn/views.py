from django.shortcuts import render
from .models import Course, Tutorial, Path, Syllabus, Guide

# Create your views here.
def home(request):
	return render(request, 'learn/home.html')
	
def courses(request):
	context = {
	'courses_web_development': Course.objects.filter(paths=1),
	'courses_personal_growth': Course.objects.filter(paths=2),
	'courses_entrepreneurship': Course.objects.filter(paths=3),
	'courses_web_design': Course.objects.filter(paths=4),
	'title': 'Courses' 
	}
	return render(request, 'learn/courses.html', context)	

def guides(request):
	context = {
	'guides': Guide.objects.all()
	}
	return render(request, 'learn/guides.html', context)


def guide_details(request, slug):
	context = {
	'guide': Guide.objects.get(slug=slug),
	}
	return render(request, 'learn/guide_details.html', context)

def course_details(request, slug):
	context = {
	'course': Course.objects.get(slug=slug),
	'title': Course.objects.get(slug=slug).course_title,
	'tutorial_shell_workshop': Tutorial.objects.filter(courses=5),
	'syllabus': Syllabus.objects.filter(course_name=Course.objects.get(slug=slug)),
	}
	return render(request, 'learn/course_details.html', context)

def courses_web_dev(request):
	context = {
	'courses_web_development': Course.objects.filter(paths=1),
	}
	return render(request, 'learn/courses_web_dev.html', context)

def courses_web_design(request):
	context = {
	'courses_web_design': Course.objects.filter(paths=4),
	}
	return render(request, 'learn/courses_web_design.html', context)


def courses_entrepreneurship(request):
	context = {
	'courses_entrepreneurship': Course.objects.filter(paths=3),
	}
	return render(request, 'learn/courses_entrepreneurship.html', context)

def courses_personal_growth(request):
	context = {
	'courses_personal_growth': Course.objects.filter(paths=2),
	}
	return render(request, 'learn/courses_personal_growth.html', context)