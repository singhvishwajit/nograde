from django.shortcuts import render
from .models import Essay, Category
	
def essays(request):
	context = {
	'essays': Essay.objects.all(),
	'essays_work': Essay.objects.filter(categories=1),
	'essays_thinking': Essay.objects.filter(categories=2),
	'essays_self_knowledge': Essay.objects.filter(categories=3),
	'essays_personal_growth': Essay.objects.filter(categories=4),
	'essays_society': Essay.objects.filter(categories=5),
	'title': 'All Essays' 
	}
	return render(request, 'learn/essays.html', context)	

def essays_work(request):
	context = {
	'essays_work': Essay.objects.filter(categories=1),
	'title': 'Essays on Work'
	}
	return render(request, 'learn/essays_work.html', context)

def essays_thinking(request):
	context = {
	'essays_thinking': Essay.objects.filter(categories=2),
	'title': 'Essays on Thinking'
	}
	return render(request, 'learn/essays_thinking.html', context)

def essays_self_knowledge(request):
	context = {
	'essays_self_knowledge': Essay.objects.filter(categories=3),
	'title': 'Essays on Self-Knowledge'
	}
	return render(request, 'learn/essays_self_knowledge.html', context)

def essays_personal_growth(request):
	context = {
	'essays_personal_growth': Essay.objects.filter(categories=4),
	'title': 'Essays on Personal Growth'
	}
	return render(request, 'learn/essays_personal_growth.html', context)

def essays_society(request):
	context = {
	'essays_society': Essay.objects.filter(categories=5),
	'title': 'Essays on Society'
	}
	return render(request, 'learn/essays_society.html', context)

def essay_details(request, slug):
	context = {
	'essay': Essay.objects.get(slug=slug),
	'title': Essay.objects.get(slug=slug).essay_title,
	}
	return render(request, 'learn/essay_details.html', context)



