from django import forms
from portfolio.models import Portfolio
from multiupload.fields import MultiFileField


class PortfolioForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=3, max_file_size=1024 * 1024 * 5)

    class Meta:
        model = Portfolio
        fields = [
            'title', 'description', 'category', 'client', 'delivery_date', 'portfolio_url', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'client': forms.TextInput(attrs={"class": "form-control"}),
            'delivery_date': forms.DateInput(attrs={"class": "form-control"}),
            'portfolio_url': forms.TextInput(attrs={"class": "form-control"}),
            'status': forms.CheckboxInput(attrs={"class": "form-control"}),
            'images': forms.FileInput(attrs={"class": "form-control"}),
        }
