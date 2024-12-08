from django.shortcuts import HttpResponse



def home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home Page</h1>")