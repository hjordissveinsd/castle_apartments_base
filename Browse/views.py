from django.shortcuts import render, redirect

from Browse.models import Estate
from Browse.models import ImageList
#kannski frekar ljótt import, skiptir pottþétt engu máli
from Browse.forms.estate_form import EstateCreateForm

# Create your views here.

#def browse(request):
 #   return render(request, 'Browse/browse.html')

def browse(request):
    context = {'estates' : Estate.objects.all().order_by('address'), 'imageList': ImageList.objects.all()}
    return render(request, 'Browse/browse.html', context )

def singleEstate(request):
    return render(request, 'Browse/single_estate.html')


def createEstate(request):
    if request.method =='POST':
        form = EstateCreateForm(data=request.POST)
        if form.is_valid():
            print('Valid!')
            form.save()
        return redirect('browse')
    else:
        form = EstateCreateForm()
    #return redirect('profile')
    return render(request, 'browse/createEstate.html', {
      'form': form
    })

def clickEstate(request):
    return render(request, 'Browse/estate_detail.html')
