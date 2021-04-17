
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('', home_page, name='home_page'),  
    path('<str:projectname>', fetch, name='fetch'),  
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

