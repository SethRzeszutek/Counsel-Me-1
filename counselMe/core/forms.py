from django import forms
from .models import Patient
from .models import Form

class PatientCreateForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			'name',
			'address',
			'insurance',
			'favorite_animal',
		]

	def is_valid(self):
		# do standard checks
		valid = super(PatientCreateForm,self).is_valid()
		return valid

class FormCreateForm(forms.ModelForm):
	class Meta:
		model = Form
		fields = [
			'name',
			'address',
			'insurance',
			'choice',
		]

	def is_valid(self):
		# do standard checks
		valid = super(FormCreateForm,self).is_valid()
		return valid
