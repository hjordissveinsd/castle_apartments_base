from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve

from Browse.models import Estate
from Browse.models import User
from Profile.models import Tracker
from Profile.views import create_track



def browse(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        estate = [{
            'id': x.id,
            'name': x.address,
            'description': x.desc,
            #zip code
        } for x in Estate.objects.filter(address__icontains=search_filter)]
        estate = list(Estate.objects.filter(address__icontains=search_filter).values())
        return JsonResponse({'data': estate})

    context = {'estates': Estate.objects.all().order_by('id')}
    current_url = resolve(request.path_info).url_name
    if current_url == 'http://127.0.0.1:8000/estate/?sort=name':
        context = {'estates': Estate.objects.all().order_by('address', )}
    return render(request, 'Browse/browse.html', context)


def singleEstate(request):
    return render(request, 'Browse/single_estate.html')


#def create_track(request, id):
    #Tracker.objects.all().delete()
    #kóði fyrir ofan notaður til að eyða efninu í töflunni
  #  track, created = Tracker.objects.get_or_create(user_id=request.user.id, estate_id=id , url=request.get_raw_uri())
    #track = Tracker()
    #track.user_id = request.user.id
    #track.url = request.get_raw_uri()
 #   if created == True:
   #     track.save()

def get_estate_by_id(request, id):
    if request.user:
        create_track(request, id)
    return render(request, 'browse/estate_detail.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })

def checkout(request, id):
    if request.GET['fname']:
        pass
    return render(request, 'Browse/checkout.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })


def payment_details(request, id):
    return render(request, 'Browse/creditcard.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })