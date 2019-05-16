from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve
from django.http import HttpResponse
from Browse.models import Estate
from Browse.models import User
from Profile.models import Tracker
#from Profile.views import create_track



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
    #if request.user:
     #   create_track(request, id)
    return render(request, 'browse/estate_detail.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })

def checkout(request, id):
    if 'firstname' in request.POST and 'email' in request.POST and 'ssn' in request.POST and 'country' in request.POST and 'street_name' in request.POST and 'house_number' in request.POST:
        firstname = request.POST['firstname']
        email =request.POST['email']
        ssn = request.POST['ssn']
        country = request.POST['country']
        street_name =request.POST['street_name']
        house_number=request.POST['house_number']
        return render(request, 'browse/checkout.html', {'firstname':firstname, 'email':email, 'ssn':ssn, 'country':country, 'street_name':street_name, 'house_number':house_number},{
            'estate':get_object_or_404(Estate,pk=id)
        })
    else:
        error=True
        return render(request, 'Browse/checkout.html', {'error':error})


def payment_details(request, id):
    return render(request, 'Browse/creditcard.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })

def order_name(request):
    search = request.GET.get('address')
    context = {'estates': Estate.objects.all().order_by('address')}

    return render(request, 'Browse/browse.html', context)

def order_price_low(request):
    search = request.GET.get('price')
    context = {'estates': Estate.objects.all().order_by('price')}

    return render(request, 'Browse/browse.html', context)

def order_price_high(request):
    search = request.GET.get('price')
    context = {'estates': Estate.objects.all().order_by('-price')}

    return render(request, 'Browse/browse.html', context)