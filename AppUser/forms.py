from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email"
        ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email"
        ]
        help_texts =  {k: "" for k in fields}

class Avatar_form(forms.Form):

    img = forms.ImageField()