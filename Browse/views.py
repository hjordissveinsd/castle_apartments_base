from django.shortcuts import render, redirect, get_object_or_404

from Browse.models import Estate
from Browse.models import ImageList
from Browse.forms.estate_form import EstateCreateForm
#kannski frekar ljótt import, skiptir pottþétt engu máli

def browse(request):
    context = {'estates' : Estate.objects.all().order_by('id'), 'imageList': ImageList.objects.all()}
    return render(request, 'Browse/browse.html', context )

def singleEstate(request):
    return render(request, 'Browse/single_estate.html')

def createEstate(request):
    if request.method =='POST':
        estate_form = EstateCreateForm(data=request.POST)
        if estate_form.is_valid():
            print('Valid!')
            estate_form.save()
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
