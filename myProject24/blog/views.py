from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q') # search keyword
    category = request.GET.get('category')# filter by category

    posts = Post.objects.all()# get all posts

    # search using Q objects
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

        # filter by category
    if category:
        posts = posts.filter(category__iexact=category)

    return render(request, 'blog/post_list.html', {'posts': posts, 'query': query, 'category': category})