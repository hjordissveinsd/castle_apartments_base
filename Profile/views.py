from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from Profile.models import User

# Create your views here.
# bætti við contex = ......
def profile(request):
    #context = {'profiles' : User.objects.all()}
    return render(request, 'Profile/profile.html')
#profile/profileMain.html', context)

def messages(request):
    return render(request, 'Profile/messages.html')

def settings(request):
    return render(request, 'Profile/settings.html')

def createOrLogIn (request):
    return render(request, 'Profile/createOrLogIn.html')

def loggedIn (request):
    return render(request, 'Profile/loggedIn.html')

def notLoggedIn (request):
    return render(request, 'Profile/notLoggedIn.html')

####################raggi######################
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request, 'profile/register.html',
                  {'form' : UserCreationForm()

                                                      }
                  )

###############################################
#raggi að bæta við#############################

#def settings(request):
#    return render(request, 'profile/profileSettings.html')