from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home page of my first djago project!')

def room(request):
    return HttpResponse('Room for each discussion')