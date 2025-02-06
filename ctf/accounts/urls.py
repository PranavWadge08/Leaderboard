from django.urls import path
from .views import (LoginView, LogoutView, SignUpView)

app_name = "accounts"

urlpatterns = [
    path('log-in/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
]
