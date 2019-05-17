from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        exclude = ['password']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['ssn', 'phone', 'avatar']
