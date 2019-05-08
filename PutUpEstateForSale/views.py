from django.shortcuts import render

# Create your views here.
def SellInput(request):
    return render(request, 'sell/sellInputForm.html')