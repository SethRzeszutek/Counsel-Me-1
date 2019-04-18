from django.contrib.auth.models import User
from django.db import models

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
