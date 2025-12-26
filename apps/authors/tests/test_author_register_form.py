from django.test import TestCase
from parameterized import parameterized

from ..forms import RegisterForm


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand(
            [
                ("username", "Your username"),
                ("email", "Your e-mail"),
                ("first_name", "Ex.: John"),
                ("last_name", "Ex.: Doe")
            ]
    )
    def test_field_placeholder(self, field, placeholder):
        form = RegisterForm()
        field_placeholder = form[field].field.widget.attrs.get("placeholder")
        self.assertEqual(field_placeholder, placeholder)
