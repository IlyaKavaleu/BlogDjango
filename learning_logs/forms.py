from django import forms
from .models import Section, Model


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['text']
        labels = {'text': ''}


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'text', 'image']
        lables = {'text': 'Model:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

