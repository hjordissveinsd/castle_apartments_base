from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve
from django.http import HttpResponse
from Browse.models import Estate, Search
from Browse.models import User
from Profile.models import Tracker
#from Profile.views import create_track
from django.db.models import Q
from Profile.views import create_track



def browse(request):

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        #raggi prófa search history
        #create_search(request, the_input="prufa")

        estate = [{
            'id': x.id,
            'name': x.address,
            'description': x.desc,
            'zip': x.zip
        } for x in Estate.objects.filter(Q(address__icontains=search_filter)| Q(zip__icontains=search_filter)| Q(city__icontains=search_filter))]
        estate = Estate.objects.filter(Q(address__icontains=search_filter)| Q(zip__icontains=search_filter)| Q(city__icontains=search_filter)).values()
        estate_list = list(estate)
        context={'data': estate_list}
        return JsonResponse(context)
    context = {'estates': Estate.objects.all().order_by('id')}
    return render(request, 'Browse/browse.html', context)


def singleEstate(request):
    return render(request, 'Browse/single_estate.html')

def get_estate_by_id(request, id):
    if request.user:
        create_track(request, id)
    return render(request, 'browse/estate_detail.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })


def create_search(request, the_input):
    #earch = Search.objects.create(user_id=1, search_input=the_input)
    search = Search()
    search.user_id= '1'
    search.search_input= "prufa"


    search.save()





def checkout(request, id):
    if 'firstname' in request.POST and 'email' in request.POST and 'ssn' in request.POST and 'country' in request.POST and 'street_name' in request.POST and 'house_number' in request.POST and 'city' in request.POST and 'zip' in request.POST and 'cardname' in request.POST and 'cardnumber' in request.POST and 'billing' in request.POST and 'expdate' in request.POST and 'cvv' in request.POST:
        firstname = request.POST['firstname']
        email =request.POST['email']
        ssn = request.POST['ssn']
        country = request.POST['country']
        street_name =request.POST['street_name']
        house_number=request.POST['house_number']
        city=request.POST['city']
        zip =request.POST['zip']
        cardname=request.POST['cardname']
        cardnumber=request.POST['cardnumber']
        billing=request.POST['billing']
        expdate=request.POST['expdate']
        cvv=request.POST['cvv']
        print('hoho')
        return render(request, 'browse/checkout.html', {'firstname':firstname, 'email':email, 'ssn':ssn, 'country':country, 'street_name':street_name, 'house_number':house_number,'city': city, 'zip':zip, 'cardname': cardname, 'cardnumber':cardnumber, 'billing':billing, 'expdate':expdate, 'cvv':cvv,
            'estate' : get_object_or_404(Estate,pk=id)
        })
    else:
        print('hello')
        error=True
        return render(request, 'Browse/checkout.html', {
            'error':error,
            'estate': get_object_or_404(Estate,pk=id)
        })


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


def successPurch(request, id):
    context = get_object_or_404(Estate, pk=id)
    context.status = False
    context.save()
    return render(request, 'Browse/purchase_success.html', {
        'estate': context
    })

def zip_filter(request):
    query = request.GET.get('search_res')
    context = {}

    if query and request.method == 'GET':
        context = Estate.objects.filter(zip=query)

    return render(request, 'Browse/browse.html', context)