from django.forms import ModelForm, widgets
from django import forms
from Browse.models import Estate
from Profile.models import User

class EstateCreateForm(ModelForm):
    class Meta:
        model = Estate
        exclude = ['id']
