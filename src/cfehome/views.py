from django.shortcuts import render
import pathlib
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).parent.resolve()

def home_page_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = page_qs.count()*100.0 / qs.count()
    except:
        percent = 0
    my_title= "My Page"
    html_template= "home.html"
    my_context= {
         "title": my_title,
          "page_visit_count": page_qs.count(),
          "percent": percent,
          "total_visit_count": qs.count()
    }
    path = request.path
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)

def old_home_page_view(request, *args, **kwargs):
     my_title= "My Home Page"
     my_context= {
          "title": my_title
     }
     html_= """
     <!DOCTYPE html>
     <html>
     <body>
     <h1>{title} anything?</h1>
     
     </body>
     </html>
     """.format(**my_context)
     return HttpResponse(html_)
    