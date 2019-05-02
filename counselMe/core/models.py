#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.db import models

class User(AbstractUser):

	# Define the extra fields
	# related to User here
	first_name = models.CharField(_('First Name of User'),
							blank = True, max_length = 20)

	last_name = models.CharField(_('Last Name of User'),
							blank = True, max_length = 20)

# More User fields according to need
	# define the custom permissions
	# related to User.
	class Meta:

		permissions = (
			("can_add_users", "Add User"),
			("can_use_form", "Able to use Form"),
			("can_view_patient", "Able to view Patient"),
			("can_edit_patient", "Able to edit Patient"),
		)


class Patient(models.Model):
	ANIMAL_CHOICES = (
		('m','Monkey'),
		('d','Dog'),
		('c','Cat'),
	)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100, null=True, blank=True)
	insurance = models.CharField(max_length=100, null=True, blank=True)
	favorite_animal = models.CharField(max_length=1, choices=ANIMAL_CHOICES, default='d')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created_ts = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Form(models.Model):
	FORM_CHOICES = (
		('y','Yes'),
		('n','No'),
		('m','Maybe'),
	)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100, null=True, blank=True)
	insurance = models.CharField(max_length=100, null=True, blank=True)
	choice = models.CharField(max_length=1, choices=FORM_CHOICES, default='m')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created_ts = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

