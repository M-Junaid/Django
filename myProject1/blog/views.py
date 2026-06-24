from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog home page")

def about(request):
    return HttpResponse("Blog about page")

