from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def browse(request):
    return render(request, 'Browse/browse.html')