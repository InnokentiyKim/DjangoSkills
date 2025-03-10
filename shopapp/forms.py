from django import forms
from django.core import validators


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2, min_value=1, max_value=100000)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}),
        label="Product description",
        validators=[validators.RegexValidator(regex=r'great', message='Must contain the word "great"'),]
    )

