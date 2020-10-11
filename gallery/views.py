from django.shortcuts import render
from .models import *

def home(request):
     images = Image.objects.all()
     category = Category.objects.all()
     locations = Location.get_location()

     if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

     elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('Category')
        images = Image.view_category(cat)

        return render(request, 'index.html', {"name":name,"images":images,"cat":cat })
     return render(request,"index.html",{'images':images,'locations':locations,'category':category})

def location_img(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_img': images})
