from django.shortcuts import render, redirect, get_object_or_404
from Browse.models import Estate
from Profile.models import User
from Sell.Forms.estate_form import EstateCreateForm
from django.http import JsonResponse
# Create your views here.


def sell(request):
  #  estate = [{
   #     'id': x.id,
    #    'name': x.address,
    #    'description': x.desc,
    #    'sold': x.status

        #zip code
    #} for x in Estate.objects.filter(owner = request.user)]
    #estate = list(Estate.objects.filter(owner = request.user).values())
    #return JsonResponse({'data': estate})

    #estate = [{
     #   'id': x.id,
      #  'name': x.address,
      #  'description': x.desc,
      #  'sold': x.status

      #zip code
  #  } for x in Estate.objects.filter(owner = request.user)]
    context = {'estates': Estate.objects.all().order_by('id')}
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
        estate_form = EstateCreateForm()
    #return redirect('profile')
    return render(request, 'createEstate.html', {
      'estate_form': estate_form
    })


#from Sell.Forms.CreateSaleForm import CreateSaleForm


#def create_sale(request):
 #   if request == 'POST':
  #      form = CreateSaleForm(data=request.POST)
   #     if form.is_valid():
    #        form.save()
    #else:
     #   form = CreateSaleForm()
      #  return render(request, 'sell/sellform.html.html', {
       #     'form' : form
        #})