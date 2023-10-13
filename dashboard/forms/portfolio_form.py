from django import forms
from django.core.exceptions import ValidationError

from portfolio.models import Portfolio, PortfolioImage, Category
from multiupload.fields import MultiFileField


class PortfolioForm(forms.ModelForm):
    image = MultiFileField(min_num=1, max_num=3, max_file_size=1024 * 1024 * 5, required=False)

    class Meta:
        model = Portfolio
        fields = [
            'title', 'description', 'category', 'client', 'delivery_date', 'portfolio_url', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": 'summernote'}),
            'category': forms.Select(attrs={"class": "form-control selectric"}),
            'client': forms.TextInput(attrs={"class": "form-control"}),
            'delivery_date': forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            'portfolio_url': forms.URLInput(attrs={"class": "form-control", "placeholder": 'example.com'}),
            'status': forms.CheckboxInput(attrs={"class": "custom-switch-input", "name": "custom-switch-checkbox"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_date'].required = False

    def clean_delivery_date(self):
        if self.instance.pk and not self.cleaned_data.get('delivery_date'):
            return self.instance.delivery_date
        return self.cleaned_data['delivery_date']


class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={"multiple": True})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
        }