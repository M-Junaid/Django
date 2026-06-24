from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    post = {
        'title': 'My 2nd Blog Template',
        'description': 'This is the description of my second blog template.',
        'author': "yes",
        'created_at': datetime.now(),
        'comments_count': 5,
        'tags': ['django', 'python', 'web development'],
        'price': 100,
        'Number': 7,
    }
    return render(request, "blog/blog_details.html",{'post':post})