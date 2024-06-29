#!/usr/bin/env python3
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    The purpose of this form is to access all the default fields + additional field age that we have added in the CustomUser model
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',) #this displays standard fields like username, password and age
        fields = (
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    """
    The purpose of this class is to access all the fields present in the UserChangeForm class.
    """

    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields #this displays standard fields
        fields = (
            "username",
            "email",
            "age",
        )
