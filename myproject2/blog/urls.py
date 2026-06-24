from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='blog-post-detail'),
    path('user/<str:username>/', views.user_profile, name='blog-user-profile'),
    path('article/<int:year>/<int:month>/', views.article_by_year_month, name='blog-article-by-year-month'),

    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name='blog-article-by-year'),
]
