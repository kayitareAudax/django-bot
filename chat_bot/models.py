from django.db import models
from django.contrib.auth.models import User
class Document(models.Model):
    text=models.TextField(max_length=100)
    file=models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.text