from django.shortcuts import render
from django.http import HttpResponse
from Browse.models import Estate

# Create your views here.

#def browse(request):
 #   return render(request, 'Browse/browse.html')

def browse(request):
    context = {'estates' : Estate.objects.all()}
    return render(request, 'Browse/browse.html', context )