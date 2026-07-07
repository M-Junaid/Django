from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username', 'Junaid', max_age=60*60*24)  # Cookie valid for 1 day
    response.set_cookie('username', 'Django Full Course', max_age=60*60*24)  # Cookie valid for 1 day
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    course = request.COOKIES.get('course', 'No course cookie found')
    # return HttpResponse(f"Username: {username}, Course: {course}")
    if 'username' in request.COOKIES:
        return HttpResponse(f"Username: {username}, Course: {course}")
    else:
        return HttpResponse("Username cookie not found")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response
