from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Whether it is completed
    completed = models.BooleanField(default=False)
# When it was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
