from django import forms

from team.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'position', 'photo', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'position': forms.Textarea(attrs={"class": 'summernote '}),
            'photo': forms.FileInput(attrs={"class": 'form-control'}),
            'icon': forms.CheckboxSelectMultiple(attrs={"class": "selectgroup-input"}),
        }