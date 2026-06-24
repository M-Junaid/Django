from django.http import HttpResponse

def post_detail(request, post_id):
    return HttpResponse(f"<h1>Show blog post: {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Show user profile: {username}</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Show articles from year: {year}</h1>")
# def article_by_year_month(request, year, month):
#     return HttpResponse(f"<h1>Show articles from {month}/{year}</h1>")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Data : {kwargs}</h1>")
