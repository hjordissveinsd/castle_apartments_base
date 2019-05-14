from django.shortcuts import render, redirect
from Browse.models import Estate

from SellEstate.forms.estate_form import EstateCreateForm

def sell(request):
    return render(request, 'sell.html')

def create_sale(request):
    return render(request, 'createEstate.html')

def createEstate(request):
    if request.method =='POST':
        estate_form = EstateCreateForm(data=request.POST)
        if estate_form.is_valid():
            #print('Valid!')
            estate_form.save()
        return redirect('sell')
    else:
        estate_form = EstateCreateForm()
    #return redirect('profile')
    return render(request, 'createEstate.html', {
      'estate_form': estate_form
    })
# Create your views here.

