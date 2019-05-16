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
        if estate_form.is_valid():
            print('Valid!')
            estate = estate_form.save(commit=False)
            estate.status = True
            estate.owner = request.user
            estate.save()
        return redirect('sell')
    else:
        print('this is in else')
        estate_form = EstateCreateForm()
    #return redirect('profile')
    return render(request, 'createEstate.html', {
      'estate_form': estate_form
    })

