from django import forms

from arrangements.models import SocIcon


class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocIcon
        fields = ['name', 'url', 'icon', 'status']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'url': forms.TextInput(attrs={"class": 'form-control'}),
            'icon': forms.RadioSelect(attrs={"class": "visually-hidden"}),
            'status': forms.CheckboxInput(attrs={"class": "custom-switch-input", "name": "custom-switch-checkbox"}),
        }