from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}

class Doctor(models.Model):
	Name = models.CharField(max_length=50)
	mobile = models.IntegerField()
	special = models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class Patient(models.Model):
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	mobile = models.IntegerField(null=True)
	address = models.TextField()

	def __str__(self):
		return self.name

class Appoinment(models.Model):
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()