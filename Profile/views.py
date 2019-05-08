from django.shortcuts import render

from Profile.models import User

# Create your views here.
# bætti við contex = ......
def profile(request):
    context = {'profiles' : User.objects.all()}
    return render(request, 'profile/profileMain.html', context)

###############################################
#raggi að bæta við#############################

#def settings(request):
#    return render(request, 'profile/profileSettings.html')