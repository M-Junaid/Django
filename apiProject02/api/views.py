from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)
