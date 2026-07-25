from django.urls import path
from .views import StudentListCreateAPI,StudentRetrieveUpdateDeleteAPI
#from .views import StudentAPI

# urlpatterns = [
#     path('student/', StudentAPI.as_view()),
#     path('students/<int:pk>/', StudentAPI.as_view())
# ]

urlpatterns = [
    path("student/", StudentListCreateAPI.as_view()),
    path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPI.as_view()),
]