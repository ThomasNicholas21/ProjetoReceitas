from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Name",
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
            }
        )
    )
    username = forms.CharField(
        label="Username",
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        max_length=128,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        )
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Password must be equal!")
