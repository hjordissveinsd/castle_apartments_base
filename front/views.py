from django.shortcuts import render
from Browse.models import Estate
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(request.GET)
    context = {'estates': Estate.objects.filter(status=True)}
    return render(request, 'front/front.html', context)


def aboutUs(request):
    return render(request, 'front/aboutus.html')