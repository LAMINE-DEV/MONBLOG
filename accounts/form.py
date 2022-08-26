from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  Profile

class SignUpForm(UserCreationForm):
	email=forms.EmailField()
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)

	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password1','password2']
		help_texts = {
            'username': None,
            'email': None,
        }



class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('profession','telephone')
