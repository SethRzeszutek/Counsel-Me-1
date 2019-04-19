from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import PatientCreateForm

from .models import Patient

PROJECT_NAME = "CounselMe"

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html', {'project_name': PROJECT_NAME})

def home(request):
	if request.method == 'GET':
		return render(request, 'home.html', {'project_name': PROJECT_NAME})

def forms(request):
	if request.method == 'GET':
		return render(request, 'forms.html', {'project_name': PROJECT_NAME})

def planner(request):
	if request.method == 'GET':
		return render(request, 'planner.html', {'project_name': PROJECT_NAME})
class PatientList(ListView):
	model = Patient
	template_name = 'patient/index.html'
	context_object_name = 'patients'
	def getProjectName(): ###I DONT THINK THIS WORKS BUT KEEPING IT HERE TO SHOW YOU
		return PROJECT_NAME

class PatientDetail(DetailView):
	model = Patient
	template_name = "patient/detail.html"
	context_object_name = 'patient'

class PatientCreate(CreateView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	form_class = PatientCreateForm
	template_name = 'patient/create.html'
	context_object_name = 'patient'

class PatientUpdate(UpdateView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	fields = ['name', 'address', 'favorite_animal', 'insurance',]
	template_name = 'patient/update.html'
	context_object_name = 'patient'

class PatientDelete(DeleteView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	template_name = 'patient/delete.html'
	context_object_name = 'patient'
