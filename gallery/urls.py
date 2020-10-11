from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns=[
  url(r'^$', views.home, name='home'),
  url(r'^location/(?P<location>\w+)/', views.location_img, name='location'),
] + static(
            settings.MEDIA_URL, 
            document_root = settings.MEDIA_ROOT
    )