from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,View
from .forms import LoginForm,RegForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.


class LoginView(FormView):
    template_name='loginpage.html'
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            email=form_data.cleaned_data.get('email')
            password=form_data.cleaned_data.get('password')
            user=authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Success')
                return redirect('homepage')
            else:
                messages.error(request,'invalid username or password')
                return render(request,'loginpage.html',{'form':form_data})


class SignupView(CreateView):
    template_name='signuppage.html'
    form_class=RegForm
    model=User
    success_url=reverse_lazy('signin')
    
    def form_valid(self,form):
        messages.success(self.request,'Signin Success')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Signin Failed')
        return super().form_valid(form)
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,'Logged out Successfully')
        return redirect('signin')