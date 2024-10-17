from django.contrib import admin
from django.urls import path, include # imported include to be able to use it in my projects url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls') ), # included my project url's url in the main url 
]
