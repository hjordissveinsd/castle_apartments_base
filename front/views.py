from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(request.GET)
    return render(request, 'front/front.html')


def aboutUs(request):
    return render(request, 'front/aboutus.html')