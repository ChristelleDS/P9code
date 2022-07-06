from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
    )
    models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserFollows', related_name='suivi')