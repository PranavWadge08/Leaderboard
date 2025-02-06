from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import SignUpForm


class LoginView(LoginView):
    """Logs User In. Extends Django's default LoginView
    from django.contrib.auth.views"""
    template_name = 'accounts/login.html'
    next_page = reverse_lazy("desk:home")


class LogoutView(LogoutView):
    """Logs User Out. Extends Django's default LogoutView
    from django.contrib.auth.views"""
    next_page = reverse_lazy("accounts:login")


class SignUpView(CreateView):
    """Sign Ups new users."""
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")
