from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def anything(request):
    return HttpResponse("This is the new app for login")

