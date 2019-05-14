from django.shortcuts import render, redirect, get_object_or_404
from Browse.models import Estate
from Sell.Forms.estate_form import EstateCreateForm
# Create your views here.


def sell(request):
    return render(request, 'sell.html')

def put_up(request):
    if request.method =='POST':
        estate_form = EstateCreateForm(data=request.POST)
        if estate_form.is_valid():
            print('Valid!')

            estate = estate_form.save()
            print(estate)
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