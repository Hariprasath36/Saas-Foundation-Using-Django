from django.shortcuts import HttpResponse
import pathlib

this_dir = pathlib.Path(__file__).parent.resolve()
def home_page_view(request, *args, **kwargs):
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
    