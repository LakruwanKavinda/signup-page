from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    app_label = 'users'  # Optional, but makes it clear which app the model belongs to
    # Add custom fields as needed
