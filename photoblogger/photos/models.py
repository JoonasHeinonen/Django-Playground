from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name        = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    image       = models.ImageField(upload_to ='uploads/')
    headline    = models.TextField(max_length=100)
    description = models.TextField(max_length=600)
    created_at  = models.DateTimeField(auto_now_add=True)