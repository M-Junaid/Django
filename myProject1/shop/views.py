from django.http import HttpResponse

def home(request):
    return HttpResponse("Shop home page")

def product(request):
    return HttpResponse("Product page of shop")

