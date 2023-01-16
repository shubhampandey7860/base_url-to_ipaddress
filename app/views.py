from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def url(request):
    return HttpResponse('url is changed')
