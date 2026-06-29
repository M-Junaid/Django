
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profile/', views.view_profile, name='view_profile'),
]
