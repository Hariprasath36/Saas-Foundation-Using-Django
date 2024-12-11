from django.shortcuts import render
import pathlib
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).parent.resolve()

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title= "My Page"
    my_context= {
         "title": my_title,
          "page_visit_count": queryset.count()
    }
    html_template= "home.html",
   
    PageVisit.objects.create()
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
    