from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
"""
3 test setups:
1) quiz
2) workdle
3) bio
"""

class QuizSetup(models.Model):
    questions = [
        'Favourite hobby',
        'Favorite animal',
        'Which place would you visit',
        'Favourite thing to do',
        'Favourite genre of music',
        'Favourite food',
        'One thing you would like to do everyday',
        'Favourite movie',
        'Favourite series',
        'How many languages do you speak',
        'Current goal in life',
    ]
    quiz_about = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.CharField(help_text=questions[0], max_length=30, blank=True, null=True)
    q2 = models.CharField(help_text=questions[1], max_length=30, blank=True, null=True)
    q3 = models.CharField(help_text=questions[2], max_length=30, blank=True, null=True)
    q4 = models.CharField(help_text=questions[3], max_length=30, blank=True, null=True)
    q5 = models.CharField(help_text=questions[4], max_length=30, blank=True, null=True)
    q6 = models.CharField(help_text=questions[5], max_length=30, blank=True, null=True)
    q7 = models.CharField(help_text=questions[6], max_length=30, blank=True, null=True)
    q8 = models.CharField(help_text=questions[7], max_length=30, blank=True, null=True)
    q9 = models.CharField(help_text=questions[8], max_length=30, blank=True, null=True)
    q10 = models.CharField(help_text=questions[9], max_length=30, blank=True, null=True)

    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quiz_about}"



class WordleSetup(models.Model):
    questions = [
        'where do you want to live',
        'What is your biggest fear',
        'What is one thing you would change about yourself',
        'favourite music genre',
        'One thing you really really really want to buy'
    ]

    quiz_about = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.CharField(help_text=questions[0], max_length=10, blank=True, null=True)
    q2 = models.CharField(help_text=questions[1], max_length=10, blank=True, null=True)
    q3 = models.CharField(help_text=questions[2], max_length=10, blank=True, null=True)
    q4 = models.CharField(help_text=questions[3], max_length=10, blank=True, null=True)
    q5 = models.CharField(help_text=questions[4], max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.quiz_about}"
