# forms.py

from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')
        labels = {
            'description': ('Description'),
            'document': ('Document')
        }

class EditDescriptionForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description']
