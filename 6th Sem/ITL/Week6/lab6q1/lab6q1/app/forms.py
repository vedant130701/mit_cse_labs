from django import forms
from django.core.management.color import Style

CHOICES=[('Kia', 'Kia'), ('BMW', 'BMW'), ('Hyundai', 'Hyundai'), ('Audi', 'Audi'), ('Ferrari', 'Ferrari'), ('Mercedes', 'Mercedes')]

class ManuFactForm(forms.Form):
    Manufacturer = forms.ChoiceField(choices=CHOICES)
    ModelName = forms.CharField()