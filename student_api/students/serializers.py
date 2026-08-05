from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "age",
            "email",
            "city",
        ]

    def validate_age(self, value):

        if value < 18:
            raise serializers.ValidationError(
                "Student must be at least 18 years old."
            )

        return value