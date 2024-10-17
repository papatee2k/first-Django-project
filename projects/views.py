from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('here are our products')

def project(request, pk):
    return HttpResponse('Single project' + ' '+ str(pk) )
