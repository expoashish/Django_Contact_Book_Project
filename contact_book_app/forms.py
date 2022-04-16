from django import forms 
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactDetailForm(forms.ModelForm): 
    class Meta: 
        model = ContactDetail
        fields = ['name', 'profile','mobile_no','address','email'];

class ContactFormMessage(ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'