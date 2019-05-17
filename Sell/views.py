from django.shortcuts import render, redirect, get_object_or_404
from Browse.models import Estate
from Profile.models import User
from Sell.Forms.estate_form import EstateCreateForm
from django.http import JsonResponse
# Create your views here.


def sell(request):
    context = {'estates': Estate.objects.filter(owner=request.user).order_by('id')}
    return render(request, 'sell.html', context)


def create_Review(request):
    context = {'estates': Estate.objects.all()}
    return render(request, 'creationReveiw.html', context)


def put_up(request):
    if request.method =='POST':
        estate_form = EstateCreateForm(request.POST, request.FILES)
        print(estate_form.errors)
        print(estate_form.is_valid())
        if estate_form.is_valid():
            print('Valid!')
            estate = estate_form.save(commit=False)
            estate.status = True
            estate.owner = request.user
            estate.save()
        return redirect('successmsg', estate.id)
    else:
        estate_form = EstateCreateForm()
        estate_form.fields['address'].label = "Address (street and street number):"
        estate_form.fields['lotSize'].label = "Lot Size (square meters):"
        estate_form.fields['houseSize'].label = "House Size (square meters):"
        estate_form.fields['bedNum'].label = "Number of bedrooms:"
        estate_form.fields['bathNum'].label = "Number of bathrooms:"
        estate_form.fields['price'].label = "Price (ISK):"
        estate_form.fields['desc'].label = "Description (write something nice about your real estate):"
        estate_form.fields['city'].label = "City and country:"
        estate_form.fields['zip'].label = "ZIP code:"
        estate_form.fields['image'].label = "Image:"
        estate_form.fields['lotSize'].type = 'number'
        estate_form.fields['houseSize'].type = 'number'
        estate_form.fields['bedNum'].type = 'number'
        estate_form.fields['bathNum'].type = 'number'
        estate_form.fields['price'].type = 'number'
        estate_form.fields['zip'].type = 'number'
    return render(request, 'createEstate.html', {
      'estate_form': estate_form
    })


def successmsg(request, id):
    return render(request, 'successSale.html', {
        'estate': get_object_or_404(Estate, pk=id)
    })
