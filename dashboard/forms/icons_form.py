from django import forms

from arrangements.models import Icons


class IconForm(forms.ModelForm):
    class Meta:
        model = Icons
        fields = ['name', 'icon_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'icon_code': forms.TextInput(attrs={'class': 'form-control'})
        }
