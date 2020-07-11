from django.forms import ModelForm
from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control user'}))
	email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control mail'}))
	password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control pass'}))
	confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control confpass'}))

class SigninForm(forms.Form):
	username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control user'}))
	password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control pass'}))