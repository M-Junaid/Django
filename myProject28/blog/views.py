from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'junaid'
    request.session['course'] = 'Django'
    return HttpResponse("Session data saved successfully.")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'No course selected')
    return HttpResponse(f"Username: {username}, Course: {course}")

def delete_session(request):
    # try:
    #     del request.session['username']
    #     del request.session['course']
    #     return HttpResponse("Session data deleted successfully.")
    # except KeyError:
    #     return HttpResponse("No session data found to delete.")
    request.session.flush() # This will delete all session data
    return HttpResponse("All session data deleted successfully.")