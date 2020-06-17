from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
