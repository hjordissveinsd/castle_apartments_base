from django.shortcuts import render, redirect, get_object_or_404
from Browse.models import Estate
from Sell.Forms.estate_form import EstateCreateForm
# Create your views here.


def sell(request):
    return render(request, 'sell.html')

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
            estate.owner = request.user.id
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