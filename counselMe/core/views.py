from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import PatientCreateForm

from .models import Patient

def login(request):
	x='hello world'
	if request.method == 'GET':
		return render(request, 'login.html', {'look_at_me': x})

def home(request):
	if request.method == 'GET':
		return render(request, 'home.html')
class PatientList(ListView):
	model = Patient
	template_name = 'patient/index.html'
	context_object_name = 'patients'

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
