from django.urls import path
from .views import student_list, create_student

urlpatterns = [
    path("students/", student_list),
    # path("students/create/", create_student),
]