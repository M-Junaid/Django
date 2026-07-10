from django.urls import path
from . import views

urlpatterns = [
    path('bulk-email/', views.bulk_email, name='bulk_email'),
]