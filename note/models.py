from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Create an instance of Topic in database."""
    topic = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

class Note(models.Model):
    """Create an instance of Note in database."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='one', null=True)
    note = models.TextField(unique=True)

    def __str__(self):
        return self.note