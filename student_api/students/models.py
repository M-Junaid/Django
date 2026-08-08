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


class Student(models.Model):
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