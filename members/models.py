from django.db import models
from django.contrib.auth.models import AbstractUser 


class Member(AbstractUser):
    reyzrs_mom = models.BooleanField(default=False)
