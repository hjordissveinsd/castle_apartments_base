from django.forms import ModelForm, widgets
from django import forms
from Browse.models import Estate

class EstateCreateForm(ModelForm):
    #image = forms.ImageField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Estate
        exclude = ['id']
        #widgets= {
            #'address' : widgets.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            #'description': widgets.TextInput(attrs={'class': 'form-control'}),
            #'price' : widgets.NumberInput(attrs={'class':'form-control'}),
            #'lotSize' : widgets.NumberInput(attrs={'class':'form-control'}),
            #'houseSize': widgets.NumberInput(attrs={'class': 'form-control'}),
            #'bedNum': widgets.NumberInput(attrs={'class': 'form-control'}),
            #'bathNum': widgets.NumberInput(attrs={'class': 'form-control'}),
            #'status': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            #'owner' : widgets.Select(attrs={'class': 'form-control'})
            #'estateType' : widgets.Select(attrs={'class':'form-control'})
            #bæta við estate type


        #}




#address = models.CharField(max_length=255) x
 #   lotSize = models.IntegerField() x
  #  houseSize = models.IntegerField() x
   # bedNum = models.IntegerField()xx
#    bathNum = models.IntegerField()x
 #   price = models.IntegerField()x
  #  desc = models.CharField(max_length=999)x
   # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #status = models.BooleanField()