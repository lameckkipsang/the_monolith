from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CuratorProfile

class CuratorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

class EditAccountForm(forms.ModelForm):
    email = forms.EmailField(disabled=True, required=True, help_text="Email cannot be changed directly.")
    class Meta:
        model = User
        fields = ['username', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CuratorProfile
        fields = ['biography', 'avatar']