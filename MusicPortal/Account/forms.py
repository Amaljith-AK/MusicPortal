from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control form-control-lg'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control form-control-lg'}))


class RegForm(UserCreationForm):
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control form-control-lg'}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control form-control-lg'}))
    class Meta:
        model=User
        fields=['first_name','last_name','username']
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'Firstname','class':'form-control form-control-lg'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Lastname','class':'form-control form-control-lg'}),
            'username':forms.EmailInput(attrs={'placeholder':'Email','class':'form-control form-control-lg'}),
        }
