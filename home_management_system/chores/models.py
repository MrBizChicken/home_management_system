from django.db import models

# Create your models here.
class Chore(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    person_to_task = models.CharField(max_length=200)
    money_earned = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
