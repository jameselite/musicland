from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *

class Addtrackform(forms.ModelForm):

    class Meta:

        model = Track
        fields = ['title', 'description', 'track', 'image',]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'titleform', 'placeholder' : 'enter the track title ...'})
        self.fields['description'].widget.attrs.update({'class' : 'descriptionform', 'placeholder' : 'enter track description ...'})
        self.fields['track'].widget.attrs.update({'class' : 'trackfileform', 'id' : 'trackform'})
        self.fields['image'].widget.attrs.update({'class' : 'imageform', 'id' : 'imageform'})



class Deletetrack(forms.Form):

    confirm = forms.BooleanField()



class Updatetrack(forms.ModelForm):

    class Meta:

        model = Track
        fields = ['title', 'description', 'track', 'image',]

        def __init__(self, *args, **kwargs):

                super().__init__(*args, **kwargs)
                self.fields['title'].widget.attrs.update({'id' : 'titleform2'})
                self.fields['description'].widget.attrs.update({'id' : 'descriptionform2'})
                self.fields['track'].widget.attrs.update({'id' : 'trackfileform2'})

class Addcomment(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['text']
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'commentform'})