from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Compliment(models.Model):
    receiver = models.CharField(max_length=100, blank=True, null=True)
    giver = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now())
    updated_date = models.DateTimeField(auto_now=True)
    # deleted_date =

    def __str__(self):
        return f"{self.receiver} Complimented by {self.giver}"
