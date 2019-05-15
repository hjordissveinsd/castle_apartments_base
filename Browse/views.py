from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Browse.models import Estate
from Browse.models import User
from Browse.forms.estate_form import EstateCreateForm
#kannski frekar ljótt import, skiptir pottþétt engu máli


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

    context = {'estates' : Estate.objects.all().order_by('id')}
    if 'name' in request.GET:
        context = {'estates' : Estate.objects.all().order_by('name')}
    return render(request, 'Browse/browse.html', context)


def singleEstate(request):
    return render(request, 'Browse/single_estate.html')


def createEstate(request):
    # TODO REMOVE THIS STUFF
    if request.method =='POST':
        #estate_form = EstateCreateForm(data=request.POST)
        estate_form = EstateCreateForm(request.POST)
        estate_image = EstateCreateForm(request.FILES)
        if estate_image:
            print("1")

        if estate_form.is_valid and estate_image.is_valid():
            print(estate_image)
            print('Valid!')
            estate_form.save()
            estate_image.save()
        return redirect('browse')
    else:
        estate_form = EstateCreateForm()
    #return redirect('profile')
    return render(request, 'browse/createEstate.html', {
      'estate_form': estate_form
    })


def get_estate_by_id(request, id):
    return render(request, 'browse/estate_detail.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })


def checkout(request):
    #context = {'estate': Estate.objects.get(pk=id)}
    return render(request, 'browse/checkout.html')


def payment_details(request, id):
    return render(request, 'Browse/creditcard.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })