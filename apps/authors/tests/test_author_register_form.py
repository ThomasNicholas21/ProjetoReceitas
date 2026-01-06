from unittest import TestCase
from parameterized import parameterized

from ..forms import RegisterForm


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand(
            [
                ("username", "Your username"),
                ("email", "Your e-mail"),
                ("first_name", "Ex.: John"),
                ("last_name", "Ex.: Doe"),
                ("password", "Your password"),
                ("confirm_password", "Repeat your password"),
            ]
    )
    def test_field_placeholder(self, field, placeholder):
        form = RegisterForm()
        field_placeholder = form[field].field.widget.attrs.get("placeholder")
        self.assertEqual(field_placeholder, placeholder)

    @parameterized.expand(
            [
                ("password", (
                        "Password must have at least one uppercase letter, "
                        "one lowercase letter and one number. The length should be "
                        "at least 8 characters."
                    )
                ),
                ("email", "The e-mail must be valid.")
            ]
    )
    def test_field_help_text(self, field, help_text):
        form = RegisterForm()
        field_help_text = form[field].field.help_text
        self.assertEqual(field_help_text, help_text)

    @parameterized.expand(
            [
                ("username", "This field must not be empty",),
                ("password", "Password must not be empty")
            ]
    )
    def test_field_error_messages_required(self, field, error_messages):
        form = RegisterForm()
        field_error_messages = form[field].field.error_messages.get("required")
        self.assertEqual(field_error_messages, error_messages)

    @parameterized.expand(
            [
                ("username", "Username",),
                ("first_name", "First name"),
                ("last_name", "Last name"),
                ("email", "E-mail"),
                ("password", "Password"),
                ("confirm_password", "Confirm Password"),
            ]
    )
    def test_field_label(self, field, error_messages):
        form = RegisterForm()
        field_label = form[field].field.label
        self.assertEqual(field_label, error_messages)

