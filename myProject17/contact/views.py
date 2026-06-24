from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact

# Create your views here.
def contact_form(request):
    return render(request, 'contact.html')

def submit_contact(request):
    name = None
    message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            contact.objects.create(name=name, message=message)
            return HttpResponse(f'Thank you for your message, {name}!')
        else:
            return HttpResponse('Please provide both name and message.')

    # If not a POST request, redirect back to the contact form
    return redirect('contact_form')

