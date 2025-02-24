from django.db import models
from django.contrib.auth.models import User
class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.session_id}"
class Chat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    message = models.TextField()
    role= models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session.title} - {self.message}"
class Document(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    pageNumber=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
