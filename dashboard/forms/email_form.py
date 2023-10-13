from django import forms

from arrangements.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'status']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={"class": "custom-switch-input", "name": "custom-switch-checkbox"}),
        }