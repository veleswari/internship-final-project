from django import forms
#from django.forms import ModelForm
from Hospital.models import Doctor,Patient,Appoinment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class DoList(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ["Name","mobile","special"]
		widgets = {
		"Name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Doctor Name"
			}),
		"mobile":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number"
			}),
		"special":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Special Field"
			}),
		}

class PoList(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ["name","gender","mobile","address"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Patient Name"
			}),
		"gender":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Gender"
			}),
		"mobile":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number"
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":3,
			}),
		}

class ApoList(forms.ModelForm):
	class Meta:
		model = Appoinment
		fields = ["doctor","patient","date","time"]
		widgets = {
		"doctor":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Doctor",
			#"empty_label":"placeholder",
			}),
		"patient":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Patient",
			}),
		"date":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Date",
			"type":"date",
			}),
		"time":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Timings",
			"type":"time",
			}),
		}