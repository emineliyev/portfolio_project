from django import forms

from arrangements.models import Arrangements


class ContactForm(forms.ModelForm):
    class Meta:
        model = Arrangements
        fields = ['address', 'phone', 'email', 'soc_icon']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'email': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'soc_icon': forms.CheckboxSelectMultiple(attrs={'class': 'selectgroup-input'}),
        }
