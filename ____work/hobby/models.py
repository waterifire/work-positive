from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from django.http import QueryDict
# Create your models here.

class Hobby(models.Model):
    hobby_user = models.ManyToManyField(User)
    hobby_name = models.ForeignKey("HobbyList", on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hobby_name}"

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"


class HobbyList(models.Model):
    hobbylist_name = models.CharField(max_length=100, blank=True, null=True)

    date_created = models.DateTimeField(default=timezone.now())
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.hobbylist_name
