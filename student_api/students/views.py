# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Student
# from .serializers import StudentSerializer

# @api_view(["GET", "POST"])
# def student_list(request):

#     if request.method == "GET":
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)

#         return Response(serializer.errors, status=400)


# @api_view(["GET", "PUT","PATCH", "DELETE"])
# def student_detail(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = StudentSerializer(student, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     if request.method == "PATCH":
#         serializer = StudentSerializer(
#         student,
#         data=request.data,
#         partial=True
#     )

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     if request.method == "DELETE":
#         student.delete()
#         return Response(status=204)

    
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class StudentDetail(APIView):

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        student = get_object_or_404(Student, id=id)

        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=204)