from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # default=False → the task is not completed when it is created.
    completed = models.BooleanField(default=False)

    # null=True → the database may have no user for an existing task.
    # blank=True → Django forms may leave the user empty.
    # on_delete=models.CASCADE → if the user is deleted, delete all their tasks as well.

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
# When it was created
    # auto_now_add=True → automatically set the field to now when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
