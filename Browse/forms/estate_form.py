from django.forms import ModelForm, widgets
from django import forms
from Browse.models import Estate

class EstateCreateForm(forms.ModelForm):
    class Meta:
        model = Estate
        exclude = ['id', 'status', 'owner']
