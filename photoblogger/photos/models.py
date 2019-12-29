from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name        = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    description = models.TextField(max_length=4000)
    image       = models.ImageField(upload_to ='uploads/')
    headline    = models.TextField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, default=55)
    updated_by  = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)