from django import forms

from services.models import Service, ServiceType


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['name', 'description', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'summernote '}),
            'icon': forms.RadioSelect(attrs={"class": "visually-hidden"}),
        }
