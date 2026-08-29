# from rest_framework import serializers
# from .models import Student


# class StudentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Student
#         fields = [
#             "id",
#             "name",
#             "age",
#             "email",
#             "city",
#         ]

#     def validate_age(self, value):

#         if value < 18:
#             raise serializers.ValidationError(
#                 "Student must be at least 18 years old."
#             )

#         return value


from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id", "owner", "name", "age", "email", "city"]
        read_only_fields = ["id"]
    
    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()

        if self.instance is not None:
            extra_kwargs["owner"] = {"read_only": True}

        return extra_kwargs

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters."
            )
        return value

    def validate_city(self, value):
        if not value:
            raise serializers.ValidationError(
                "City is required."
            )
        return value

    def validate_age(self, value):
        if value < 18 or value > 60:
            raise serializers.ValidationError(
                "Student must be between 18 and 60 years old."
            )
        return value