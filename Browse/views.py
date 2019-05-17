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
from django.contrib.auth.decorators import login_required


def filter_(request):
    bath_min = request.GET.get('bath_min', '')
    bath_max = request.GET.get('bath_max', '')
    bed_min = request.GET.get('bed_min', '')
    bed_max = request.GET.get('bed_max', '')
    zip_min = request.GET.get('zip_min', '')
    zip_max = request.GET.get('zip_max', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')

    filter_ = Q(status=True)
    print('heyyy')
    if bath_min:
        filter_ &= Q(bathNum__gte=bath_min)
    if bath_max:
        filter_ &= Q(bathNum__lte=bath_max)
    if bed_min:
        filter_ &= Q(bedNum__gte=bed_min)
    if bed_max:
        filter_ &= Q(bedNum__lte=bed_max)
    if zip_min:
        filter_ &= Q(zip__gte=zip_min)
    if zip_max:
        filter_ &= Q(zip__lte=zip_max)
    if price_min:
        filter_ &= Q(price__gte=price_min)
    if price_max:
        filter_ &= Q(price__lte=price_max)

    print('query = ', filter_)

    estates = Estate.objects.filter(filter_).values()
    print('estates = ', estates)
    estate_list = list(estates)
    print('estate_list = ', estate_list)
    jsonstring = {'data': estate_list}
    return JsonResponse(jsonstring)



def browse(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        create_search(request, the_input=search_filter)

        estate_filter = Q(status=True)
        estate_or = Q(address__icontains=search_filter)| Q(zip__icontains=search_filter)| Q(city__icontains=search_filter)
        estate_filter &= estate_or
        estate = Estate.objects.filter(estate_filter).values()
        estate_list = list(estate)
        jsonstring={'data': estate_list}
        return JsonResponse(jsonstring)


    context = {'estates': Estate.objects.all().order_by('-id')}
    return render(request, 'Browse/browse.html', context)


def singleEstate(request):
    return render(request, 'Browse/singleEstate.html')

def get_estate_by_id(request, id):

    create_track(request, id)
    return render(request, 'browse/estateDetail.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })



@login_required
def create_search(request, the_input):
    search, created = Search.objects.get_or_create(user_id=request.user.id, search_input=the_input)
    if created:
        search.save()



def checkout(request, id):

    if request.POST:
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
            return render(request, 'browse/checkOut.html', {'firstname':firstname, 'email':email, 'ssn':ssn, 'country':country, 'street_name':street_name, 'house_number':house_number, 'city': city, 'zip':zip, 'cardname': cardname, 'cardnumber':cardnumber, 'billing':billing, 'expdate':expdate, 'cvv':cvv,
                'estate' : get_object_or_404(Estate,pk=id)
                                                            })
        else:
            return redirect('/estate')
    return redirect('/estate')



def payment_details(request, id):
    estate = get_object_or_404(Estate, pk=id)
    if estate.owner_id != request.user.id:
        context = {'estate': estate}
        return render(request, 'Browse/creditCard.html', context)
    return redirect('/estate')


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
    return render(request, 'Browse/purchaseSuccess.html', {
        'estate': context
    })

def zip_filter(request):
    query = request.GET.get('search_res')
    context = {}

    if query and request.method == 'GET':
        context = Estate.objects.filter(zip=query)

    return render(request, 'Browse/browse.html', context)