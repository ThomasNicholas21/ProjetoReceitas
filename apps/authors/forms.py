import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


def validate_password(password):
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$")
    if not regex.match(password):
        raise ValidationError(
            "Not a strong password!",
            code="invalid"
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "Your username")
        add_placeholder(self.fields["email"], "Your e-mail")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["last_name"], "Ex.: Doe")

    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Your password"
        }),
        error_messages={
            "required": "Password must not be empty"
        },
        help_text=(
            "Password must have at least one uppercase letter, "
            "one lowercase letter and one number. The length should be "
            "at least 8 characters."
        ),
        validators=[validate_password,]
    )
    confirm_password = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Repeat your password"
        })
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
        labels = {
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "email": "E-mail",
        }
        help_texts = {
            "email": "The e-mail must be valid.",
        }
        error_messages = {
            "username": {
                "required": "This field must not be empty",
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            password_must_be_equal = ValidationError("Both password must be equal!")
            raise ValidationError(
                {
                    "password": password_must_be_equal,
                    "confirm_password": password_must_be_equal,
                }
            )

        return cleaned_data
