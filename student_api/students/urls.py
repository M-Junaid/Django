# from django.urls import path

# from .views import StudentDetail, StudentList

# urlpatterns = [
#     path("students/", StudentList.as_view(), name="student-list"),
#     path("students/<int:id>/", StudentDetail.as_view(), name="student-detail"),
# ]


from django.urls import path
# from .views import StudentList, StudentDetail

# urlpatterns = [
#     path("students/", StudentList.as_view()),
#     path("students/<int:pk>/", StudentDetail.as_view()),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register("students", StudentViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
]