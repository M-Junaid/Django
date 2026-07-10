from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache

def user_list(request):
    user = cache.get('user_data')
    if not users:
        print('Cache miss: Fetching data form database')
        user = YoutubeUser.objects.all()
        cache.set('user_data', users, timeout=60) # Cache data for 60 second
    else:
        print('Cache hit: Feteching data form cache')
    return render(request, 'user_list.html', {'users': user})



