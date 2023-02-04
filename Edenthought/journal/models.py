from django.db import models
from django.forms import CharField

# Create your models here.

from django.contrib.auth.models import User


class Thought(models.Model):
    title = models.CharField(max_length=85)
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True)
