from django import forms

from team.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'position', 'photo', 'soc_network_facebook', 'soc_network_instagram', 'soc_network_linkedin',
                  'soc_network_twitter']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'position': forms.TextInput(attrs={"class": 'form-control '}),
            'photo': forms.FileInput(attrs={"class": 'form-control'}),
            'soc_network_facebook': forms.TextInput(attrs={"class": 'form-control '}),
            'soc_network_instagram': forms.TextInput(attrs={"class": 'form-control '}),
            'soc_network_linkedin': forms.TextInput(attrs={"class": 'form-control '}),
            'soc_network_twitter': forms.TextInput(attrs={"class": 'form-control '}),
        }
