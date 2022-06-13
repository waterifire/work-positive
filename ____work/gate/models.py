from django.db import models

from django.utils import timezone
# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.CharField(help_text='not email password, random one',max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.CharField(max_length=100, blank=True, null=True) 

    # Choose image here

    # for talk to me about
    like1 = models.CharField(max_length=100, blank=True, null=True)
    like2 = models.CharField(max_length=100, blank=True, null=True)
    like3 = models.CharField(max_length=100, blank=True, null=True)
    like4 = models.CharField(max_length=100, blank=True, null=True)

    # for hobbies
    hobby1 = models.CharField(max_length=100, blank=True, null=True)
    hobby2 = models.CharField(max_length=100, blank=True, null=True)
    hobby3 = models.CharField(max_length=100, blank=True, null=True)
    hobby4 = models.CharField(max_length=100, blank=True, null=True)

    updated = models.DateTimeField(default=timezone.now(), blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
