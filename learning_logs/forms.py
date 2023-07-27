from django import forms
from .models import Section, Model


class SectionForm(forms.ModelForm):
    """Form for model Section"""
    class Meta:
        model = Section
        fields = ['text']
        labels = {'text': ''}


class ModelForm(forms.ModelForm):
    """Form for model Model"""
    class Meta:
        model = Model
        fields = ['name', 'text', 'image']
        lables = {'text': 'Model:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

