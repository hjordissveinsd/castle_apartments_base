from django.shortcuts import render
from Browse.models import Estate
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(request.GET)
    context = {'estates': Estate.objects.filter(status=True)[:4]}
    return render(request, 'front/front.html', context)


def about_us(request):
    return render(request, 'front/aboutUs.html')

def teenage(request):
    context = {'estates': Estate.objects.filter(status=True)[:4]}
    return render(request, 'front/teenage.html', context)

def texas(request):
    context = {'estates': Estate.objects.filter(status=True)[:4]}
    return render(request, 'front/texas.html', context)
