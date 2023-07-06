from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'single-item text-field'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'single-item text-field'}))


class RegForm(UserCreationForm):
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'single-item text-field'}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'single-item text-field'}))
    class Meta:
        model=User
        fields=['first_name','last_name','username']
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'Firstname','class':'single-item text-field'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Lastname','class':'single-item text-field'}),
            'username':forms.EmailInput(attrs={'placeholder':'Email','class':'single-item text-field'}),
        }
