from django import forms
from django.core.exceptions import ValidationError

from about.models import About, BusinessPlan, Partners


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'summernote'})
        }


class BusinessPlaneForm(forms.ModelForm):
    class Meta:
        model = BusinessPlan
        fields = ['title', 'description', 'icon']
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'form-control '}),
            'icon': forms.RadioSelect(attrs={"class": "visually-hidden"}),
        }


class PartnersForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ['image', 'active']
        widgets = {
            'image': forms.FileInput(attrs={"class": 'form-control'}),
            'active': forms.CheckboxInput(attrs={"class": 'custom-switch-input', "name": "custom-switch-checkbox"}),
        }
