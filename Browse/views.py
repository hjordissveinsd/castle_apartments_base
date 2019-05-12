from django.shortcuts import render

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
    return render(request, 'Browse/single_estate.html.html')


def createEstate(request):
    if request.method =='POST':
        print(1)
    else:
        form = EstateCreateForm()
    return render(request, 'browse/createEstate.html', {
      'form': form

    })
