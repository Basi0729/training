from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Profile
from articles.forms import *




def home_view(request):
 
 profile_queryset=Profile.objects.all()
 
 HTML_STRING= render_to_string("home.-view.html",
  {"object_list2": profile_queryset}
)
 return HttpResponse(HTML_STRING)

 
