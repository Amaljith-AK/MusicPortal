from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView,FormView
from .models import SongsModel
from .forms import AddSongsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# decorator

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
    return inner
dec=[signin_required,never_cache]


# Create your views here.
@method_decorator(dec,name='dispatch')
class MusicHomeView(ListView):
    template_name='index.html'
    model=SongsModel
    context_object_name='songs'

    def get_queryset(self):
        return SongsModel.objects.filter(upload_type='public') | SongsModel.objects.filter(upload_type='private',user=self.request.user) | SongsModel.objects.filter(Q(share_to=self.request.user.username) | Q(user=self.request.user),upload_type='protected')
        
@method_decorator(dec,name='dispatch')
class PrivateSongView(ListView):
    template_name='privatesong.html'
    models=SongsModel
    context_object_name='privatesongs'

    def get_queryset(self):
        return SongsModel.objects.filter(user=self.request.user,upload_type='private')
    

@method_decorator(dec,name='dispatch')
class SharedSongView(ListView):
    template_name='sharedsong.html'
    model=SongsModel
    context_object_name='sharedsongs'

    def get_queryset(self):
        return SongsModel.objects.filter(Q(share_to=self.request.user.username) | Q(user=self.request.user),upload_type='protected')

@method_decorator(dec,name='dispatch')
class AddSongsView(FormView):
    template_name='addmusic.html'
    form_class=AddSongsForm

    def post(self,request,*args,**kwargs):
        us=request.user
        form_data=AddSongsForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            singers=form_data.cleaned_data.get('singers')
            image=form_data.cleaned_data.get('image')
            song=form_data.cleaned_data.get('song')
            upload_type=form_data.cleaned_data.get('upload_type')
            share_to=form_data.cleaned_data.get('share_to')    
            if upload_type == 'protected':
                for i in User.objects.all():
                    if share_to == i.username:
                        SongsModel.objects.create(title=title,singers=singers,user=us,image=image,song=song,upload_type=upload_type,share_to=share_to)
                        messages.success(request,'Song Added Successfully')
                        return redirect('homepage')    
                return render(request,'addmusic.html',{'form':form_data})
            else:
                SongsModel.objects.create(title=title,singers=singers,user=us,image=image,song=song,upload_type=upload_type)
                messages.success(request,'Song Added Successfully')
                return redirect('homepage')
        else:
            messages.error(request,'Song Adding Failed')
            return render(request,'addmusic.html',{'form':form_data})