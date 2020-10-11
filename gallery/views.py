from django.shortcuts import render
from .models import Image,Location

def home(request):
     images = Image.objects.all()
     locations = Location.get_location()

     return render(request, "index.html",{'images':images,'locations':locations})