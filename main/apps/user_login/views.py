from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
	context = {
		"users": User.objects.all(),
	}	
	return render(request, 'user_login/index.html', context)


def new(request):
	return render(request, 'user_login/new.html')

def new_create(request, methods=['POST']):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error, extra_tags=tag)
			request.session['error'] = error	
		return redirect('/new')	
	else:
		request.session.delete()
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		return redirect('/')


def edit(request, id):
	context = {
		"user_id": User.objects.get(id=id),
	}
	return render(request, 'user_login/edit.html', context)


def update(request, id, methods=['POST']):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')	
	else:
		user = User.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('/')


def show(request, id):
	context = {
		"user_id": User.objects.get(id=id),
	}
	return render(request, 'user_login/show.html', context)


def delete(request, id):
	b = User.objects.get(id=id)
	b.delete()
	return redirect('/')	 