from django import forms

from arrangements.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone', 'status']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control phone-number'}),
            'status': forms.CheckboxInput(attrs={"class": "custom-switch-input", "name": "custom-switch-checkbox"}),
        }