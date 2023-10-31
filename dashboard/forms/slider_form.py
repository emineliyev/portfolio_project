from django import forms

from slider.models import Slider


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'description', 'image', 'css_selector', 'status']
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'form-control'}),
            'image': forms.FileInput(attrs={"class": 'form-control'}),
            'css_selector': forms.TextInput(attrs={"class": 'form-control'}),
            'status': forms.CheckboxInput(attrs={"class": "custom-switch-input", "name": "custom-switch-checkbox"}),
        }