from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def favorite_sports(request):
    return HttpResponse('Soccer, Baseball')
