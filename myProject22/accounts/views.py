from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages


def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error uplaoding profile picture. Please try agian ' )
        
    else:
        form = ProfileForm()
    return render(request, 'accounts/uploading_profile.html', {'form': form})    




# Create your views here.

