from django import forms
from .models import Patient

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
