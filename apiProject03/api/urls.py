# from django.urls import path
# from .views import StudentListCreateAPI,StudentRetrieveUpdateDeleteAPI
#from .views import StudentAPI

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet 

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]



# urlpatterns = [
#     path('student/', StudentAPI.as_view()),
#     path('students/<int:pk>/', StudentAPI.as_view())
# ]

# urlpatterns = [
#     path("student/", StudentListCreateAPI.as_view()),
#     path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPI.as_view()),
# ]