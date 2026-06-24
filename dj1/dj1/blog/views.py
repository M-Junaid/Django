from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('welcome to my blog page!')

def about(request):
    return HttpResponse('welcome to about page!')
