from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_list(request):
    blogs = [
         
           { 'title' : 'Django Basic Tutorial','is_featured':True, 'author':'junaid'},
           { 'title' : 'Django Advance Tutorial','is_featured':False, 'author':''},
           { 'title' : 'Django Rest Framework Tutorial','is_featured':True, 'author':'ahmed'},

        
    ]
    context = { 
        "blogs" : blogs,
        "today": datetime.now(),
        "html_code": "<h1>Welcome To My Blog</h1>"
    }
    return render(request, "blog/blog_list.html", context)