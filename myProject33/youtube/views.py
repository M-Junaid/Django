from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache

def user_list(request):
    users = cache.get('user_data')
    if not users:
        print('Cache miss: Fetching data from database')
        users = YoutubeUser.objects.all()
        cache.set('user_data', users, timeout=60)  # Cache data for 60 seconds
    else:
        print('Cache hit: Fetching data from cache')
    return render(request, 'user_list.html', {'users': users})




