from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index():
    return HttpResponse("Hi i am django")