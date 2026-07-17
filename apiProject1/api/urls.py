from django.urls import path
from .views import student_list
from . import views

urlpatterns = [
    path('student/', views.student_list, name='student_list'),
]