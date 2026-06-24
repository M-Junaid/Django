from django.shortcuts import render
from datetime import datetime


class User:
    def __init__(self, name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': 'Junaid',
        'age': 25,
        'skills': ['Python', 'Django', 'JavaScript'],
        'current_time': datetime.now(),
        'user': User('Ramzan', 27),
        'blog':{
            'title': 'django template intro',
            'author': {
                'name': 'Junaid',
                
                
            },
            'content': '<b>This is a blog post about Django templates.</b>',
            'created_at' : datetime(2026, 2, 13, 4, 14)
            
        },
        'empty_value': None,
    }
    return render(request, 'blog/home.html', context)

# Create your views here.
