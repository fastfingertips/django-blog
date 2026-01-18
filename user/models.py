from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for future flexibility.
    Add any extra fields here (e.g., bio, profile_picture).
    """

    objects: models.Manager

    class Theme(models.TextChoices):
        LIGHT = 'light', 'Light Theme'
        DARK = 'dark', 'Dark Theme'

    theme_preference = models.CharField(
        max_length=10,
        choices=Theme.choices,
        default=Theme.LIGHT,
    )
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.username)
