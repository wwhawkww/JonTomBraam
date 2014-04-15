from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.template import TemplateDoesNotExist


def home(request):
	#template = loader.get_template('templates/Baseplate.html')
	#return render_to_response(request, template)
	poll = 'polls'
	return render(request, 'Home.html', {'poll': poll})

def aboutme(request):
	poll = 'polls'
	return render(request, 'AboutMe.html', {'poll':poll})

def blog(request):
	poll = 'polls'
	return render(request, 'Blog.html', {'poll':poll})

def projects(request):
	poll = 'polls'
	return render(request, 'Projects.html', {'poll':poll})

def resume(request):
	poll = 'polls'
	return render(request, 'Resume.html', {'poll':poll})