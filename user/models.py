from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme_preference = models.CharField(
        max_length=255,
        choices=[("light", "Light Theme"), ("dark", "Dark Theme")]
        )