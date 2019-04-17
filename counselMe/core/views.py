from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def home(request):
	x='hello world'
	if request.method == 'GET':
		return render(request, 'home.html', {'look_at_me': x})