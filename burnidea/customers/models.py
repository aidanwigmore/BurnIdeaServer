from django.conf import settings
import re

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.authtoken.models import Token as DefaultToken

# Create your models here.

class CustomerManager(BaseUserManager):
    def create_user(self, email, name, given_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not self.is_valid_password(password):
            raise ValueError('Password must be at least 8 characters long and contain at least 3 special characters and 3 digits')
        email = self.normalize_email(email)
        user = self.model (email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, given_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, given_name, password, **extra_fields)

    def is_valid_password(self, password):
        if len(password) < 8:
            return False
        if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 3:
            return False
        if len(re.findall(r'\d', password)) < 3:
            return False
        return True

class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100, blank=True, null=True)

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subscribed_to_newsletter = models.BooleanField(default=False)
    sms_notifications = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'given_name']

    def __str__(self):
        return self.email

    class QuickConfig:
        name = 'customer'
        mutable_fields = ['name', 'given_name', 'phone_number', 'subscribed_to_newsletter', 'sms_notifications', 'email_notifications']
