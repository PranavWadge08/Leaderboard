from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    """Create form for user creation."""
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('ticket_id', 'first_name', 'last_name',
                  'mobile', 'email', 'occupation', 'password1',
                  'password2',)
