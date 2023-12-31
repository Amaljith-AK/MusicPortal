from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import SongsModel

class AddSongsForm(forms.ModelForm):
    class Meta:
        model=SongsModel
        fields=['title','singers','image','song','upload_type','share_to']
        widgets={
            'title':forms.TextInput(attrs={'class':'single-item text-field','placeholder':'Title'}),
            'singers':forms.TextInput(attrs={'class':'single-item text-field','placeholder':'Singers'}),
            'image':forms.FileInput(attrs={'class':'single-item text-field up-btn'}),
            'song':forms.FileInput(attrs={'class':'single-item text-field up-btn'}),
            'upload_type':forms.Select(attrs={'class':'single-item text-field dark-field'}),
            'share_to':forms.EmailInput(attrs={'class':'single-item text-field','placeholder':'Only if Type is Protected'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddSongsForm,self).__init__(*args,**kwargs)
        self.fields['share_to'].required=False

    def clean(self):
        upt=self.cleaned_data.get('upload_type')
        sht=self.cleaned_data.get('share_to')
        if upt == 'protected' and sht is None:
            def __init__(self,*args,**kwargs):
                super(AddSongsForm,self).__init__(*args,**kwargs)
                self.fields['share_to'].required=True
            msg='Email of Person to share the song is necessary'
            self.add_error('share_to',msg)
        return super().clean()