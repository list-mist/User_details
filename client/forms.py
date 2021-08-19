from django import forms
from django.forms.widgets import PasswordInput

class Login(forms.Form): 
    email=forms.EmailField()
    password=forms.CharField(widget=PasswordInput)

class Signup(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=PasswordInput)
    confirm_password=forms.CharField(widget=PasswordInput)
    address=forms.CharField()
    
