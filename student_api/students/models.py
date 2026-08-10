# from django.db import models

# class Student(models.Model):

#     name = models.CharField(max_length=100)

#     age = models.IntegerField()

#     email = models.EmailField(unique=True)

#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Student(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="students",
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=100)

    age = models.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(60),
        ]
    )

    email = models.EmailField(unique=True)

    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name