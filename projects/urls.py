from django.urls import path # To link it to the main url
from . import views # To be able to add views functions to projects url


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
]
