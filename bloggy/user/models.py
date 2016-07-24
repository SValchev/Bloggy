from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_superuser, is_staff, **extra_fields):
        """
        Creates and saves a User with the given username,  email and password.
        """
        username = username or email
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username=None,  **extra_fields):
        return self._create_user(username, email, password, is_staff=False ,is_superuser=False, **extra_fields)

    def create_superuser(self, email, password, username=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255, blank=True)
    email = models.EmailField(unique=True, max_length=225)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
