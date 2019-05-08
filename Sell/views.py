from django.shortcuts import render

# Create your views here.


def sell(request):
    return render(request, 'sell/sell.html')


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