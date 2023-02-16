from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    class Status(models.TextChoices):
        STATUS_CLOSED = 'closed'
        STATUS_OPEN = 'open'
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.TextField(default='')
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=Status.choices, default='open')


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True,)
    body = models.TextField(blank=True, default='')