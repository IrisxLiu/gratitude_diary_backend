""" Form generated based on Joy model to handle its data"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Joy


class JoyForm(forms.ModelForm):
    """ class JoyForm, inherit forms.ModelForm """
    class Meta:
        """ Metadata of the form
            The form uses Joy model and its title and desc fields
        """
        model = Joy
        fields = ['title', 'desc']

    def __init__(self, *args, **kwargs):
        """ Override init method with placeholders """
        super(JoyForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs["placeholder"] = "Highlight"
        self.fields['desc'].widget.attrs["placeholder"] = "Illustrate \
the story behind you smile"


class UserForm(UserCreationForm):
    """ class UserForm, inherit UserCreationForm """
    class Meta:
        """ Metadata of the form
            The form uses User model and
            its username, email, password1, passwords2 fields
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
