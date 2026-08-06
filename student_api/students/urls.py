from django.urls import path

from .views import StudentDetail, StudentList

urlpatterns = [
    path("students/", StudentList.as_view(), name="student-list"),
    path("students/<int:id>/", StudentDetail.as_view(), name="student-detail"),
]