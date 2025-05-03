from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, Permission
from school.validators import *

class UserManager(BaseUserManager):
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


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(
        max_length=10,
        validators=[phone_validator],
        help_text="Enter a 10-digit contact number",
    )
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255)
    
   
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
    def __str__(self):
        return self.email