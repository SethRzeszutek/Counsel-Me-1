from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import PatientCreateForm
from .forms import FormCreateForm

from .models import Patient
from .models import Form

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
	project_name = PROJECT_NAME
	def __str__(self):
		return self.project_name

class PatientView(DetailView):
	model = Patient
	template_name = "patient/patient_view.html"
	context_object_name = 'patient'

class PatientCreate(CreateView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	form_class = PatientCreateForm
	template_name = 'patient/patient_create.html'
	context_object_name = 'patient'

class PatientEdit(UpdateView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	fields = ['name', 'address', 'favorite_animal', 'insurance',]
	template_name = 'patient/patient_edit.html'
	context_object_name = 'patient'

class PatientDelete(DeleteView):
	model = Patient
	success_url = reverse_lazy('core:patient_index')
	template_name = 'patient/patient_delete.html'
	context_object_name = 'patient'



class FormList(ListView):
	model = Form
	template_name = 'form/form_index.html'
	context_object_name = 'forms'

class FormCreate(CreateView):
	model = Form
	success_url = reverse_lazy('core:form_index')
	form_class = FormCreateForm
	template_name = 'form/form_create.html'
	context_object_name = 'form'

class FormView(DetailView):
	model = Form
	template_name = "form/form_view.html"
	context_object_name = 'form'

class FormEdit(UpdateView):
	model = Form
	success_url = reverse_lazy('core:form_index')
	fields = ['name', 'address', 'choice', 'insurance',]
	template_name = 'form/form_edit.html'
	context_object_name = 'form'

class FormDelete(DeleteView):
	model = Form
	success_url = reverse_lazy('core:form_index')
	template_name = 'form/form_delete.html'
	context_object_name = 'form'
