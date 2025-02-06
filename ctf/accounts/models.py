from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    EMAIL_VALIDATOR = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    MOBILE_VALIDATOR = RegexValidator(
        regex=r'^[6-9][0-9]{9}$',
        message="Phone number must be entered in the format: '9090000900'. \
             Only 10 digits allowed.")
    ticket_id = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)
    email = models.CharField(
        max_length=255, validators=[EMAIL_VALIDATOR], unique=True)
    mobile = models.CharField(
        validators=[MOBILE_VALIDATOR], max_length=15, unique=True, blank=True, null=True)
    occupation = models.CharField(max_length=50, help_text="Job role/Course(if studing)")
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["ticket_id"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
