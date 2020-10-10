from django.shortcuts import render
from .models import Image

def home(request):
     context = {}
     images = Image.objects.all()
     context['images'] = images

     return render(request, "index.html", context)